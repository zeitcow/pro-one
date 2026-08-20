#!/usr/bin/env python3
"""Validate Pro-One schemas, sample records, references, and repository invariants."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
DATA_DIR = ROOT / "data"

DATA_SCHEMAS = {
    "sample-evaluation-fixtures.json": ("evaluation_fixture", "evaluation-fixture.schema.json"),
    "sample-intakes.json": ("intake", "intake.schema.json"),
    "sample-legal-documents.json": ("legal_document", "legal-document.schema.json"),
    "sample-legal-rules.json": ("legal_rule", "legal-rule.schema.json"),
    "sample-process-steps.json": ("process_step", "process-step.schema.json"),
    "sample-responses.json": ("response", "response.schema.json"),
    "sample-risks.json": ("risk", "risk.schema.json"),
    "sample-sources.json": ("source", "source.schema.json"),
    "sample-workflows.json": ("workflow", "workflow.schema.json"),
}

REFERENCE_FIELDS = {
    "source_ids": "source",
    "required_source_ids": "source",
    "optional_source_ids": "source",
    "allowed_source_ids": "source",
    "prohibited_source_ids": "source",
    "deadline_source_ids": "source",
    "superseded_by_source_id": "source",
    "workflow_ids": "workflow",
    "supported_workflow_ids": "workflow",
    "process_step_ids": "process_step",
    "supported_process_step_ids": "process_step",
    "previous_step_ids": "process_step",
    "next_step_ids": "process_step",
    "legal_document_ids": "legal_document",
    "document_ids": "legal_document",
    "supported_document_ids": "legal_document",
    "legal_rule_ids": "legal_rule",
    "required_rule_ids": "legal_rule",
    "optional_rule_ids": "legal_rule",
    "risk_ids": "risk",
    "expected_risk_ids": "risk",
    "evaluation_fixture_ids": "evaluation_fixture",
    "required_evaluation_fixture_ids": "evaluation_fixture",
    "response_ids": "response",
}

DISALLOWED_DEPENDENCY_STATES = {"deprecated", "rejected"}
MOJIBAKE_MARKERS = ("\ufffd", "\u00e2\u20ac", "\u00c3", "\u00c2")


class ValidationReport:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.counts: defaultdict[str, int] = defaultdict(int)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def checked(self, category: str, amount: int = 1) -> None:
        self.counts[category] += amount


def load_json(path: Path, report: ValidationReport) -> Any | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.error(f"{path.relative_to(ROOT)}: invalid JSON/UTF-8: {exc}")
        return None
    report.checked("JSON files")
    return value


def json_path(parts: Iterable[Any]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def walk_references(value: Any, path: tuple[Any, ...] = ()):
    if isinstance(value, dict):
        for key, child in value.items():
            current = path + (key,)
            target_kind = REFERENCE_FIELDS.get(key)
            if target_kind:
                if isinstance(child, list):
                    for index, record_id in enumerate(child):
                        if isinstance(record_id, str):
                            yield target_kind, record_id, current + (index,)
                elif isinstance(child, str):
                    yield target_kind, child, current
            yield from walk_references(child, current)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_references(child, path + (index,))


def validate_markdown(report: ValidationReport) -> None:
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    fence_pattern = re.compile(r"^\s*(`{3,}|~{3,})")

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            report.error(f"{path.relative_to(ROOT)}: invalid UTF-8 Markdown: {exc}")
            continue

        report.checked("Markdown files")
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                report.error(f"{path.relative_to(ROOT)}: possible encoding corruption marker {marker!r}")

        open_fence: tuple[str, int] | None = None
        for number, line in enumerate(text.splitlines(), start=1):
            match = fence_pattern.match(line)
            if not match:
                continue
            marker = match.group(1)[0]
            if open_fence is None:
                open_fence = (marker, number)
            elif open_fence[0] == marker:
                open_fence = None
        if open_fence:
            report.error(
                f"{path.relative_to(ROOT)}:{open_fence[1]}: unclosed {open_fence[0] * 3} fence"
            )

        for match in link_pattern.finditer(text):
            destination = match.group(1).strip().strip("<>")
            destination = destination.split(maxsplit=1)[0]
            if not destination or destination.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_path = destination.split("#", 1)[0]
            if local_path and not (path.parent / local_path).resolve().exists():
                line = text.count("\n", 0, match.start()) + 1
                report.error(
                    f"{path.relative_to(ROOT)}:{line}: broken relative link {destination!r}"
                )


def review_status(record: dict[str, Any]) -> str | None:
    review = record.get("review")
    return review.get("status") if isinstance(review, dict) else None


def maturity_status(record: dict[str, Any]) -> str | None:
    return record.get("status")


def is_supported(record: dict[str, Any]) -> bool:
    return maturity_status(record) == "supported"


def validate_review_provenance(
    filename: str, record: dict[str, Any], report: ValidationReport
) -> None:
    review = record.get("review")
    if not isinstance(review, dict):
        return
    if review.get("status") in {"reviewed", "approved"}:
        required = (
            "reviewed_by",
            "reviewer_role",
            "review_scope",
            "reviewed_on",
            "reviewed_record_version",
        )
        missing = [field for field in required if not review.get(field)]
        if missing:
            report.error(
                f"{filename}:{record.get('id')}: reviewed/approved record lacks review provenance: "
                + ", ".join(missing)
            )
        if review.get("reviewed_record_version") != record.get("record_version"):
            report.error(
                f"{filename}:{record.get('id')}: review version does not match record_version"
            )


def main() -> int:
    report = ValidationReport()

    parsed_json: dict[Path, Any] = {}
    for path in sorted(ROOT.rglob("*.json")):
        if ".git" not in path.parts:
            value = load_json(path, report)
            if value is not None:
                parsed_json[path] = value

    schemas: dict[str, dict[str, Any]] = {}
    registry = Registry()
    for path in sorted(SCHEMA_DIR.glob("*.json")):
        schema = parsed_json.get(path)
        if not isinstance(schema, dict):
            continue
        try:
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
        except Exception as exc:  # check_schema raises several detailed exception types
            report.error(f"{path.relative_to(ROOT)}: invalid Draft 2020-12 schema: {exc}")
            continue
        schemas[path.name] = schema
        report.checked("JSON Schemas")

    records_by_kind: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    record_locations: dict[tuple[str, str], str] = {}

    for filename, (kind, schema_name) in DATA_SCHEMAS.items():
        path = DATA_DIR / filename
        records = parsed_json.get(path)
        schema = schemas.get(schema_name)
        if not isinstance(records, list):
            report.error(f"data/{filename}: expected a JSON array")
            continue
        if schema is None:
            report.error(f"data/{filename}: schema {schema_name} was not available")
            continue

        validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                report.error(f"data/{filename}[{index}]: expected an object")
                continue
            record_id = record.get("id")
            if not isinstance(record_id, str):
                report.error(f"data/{filename}[{index}]: missing string id")
                continue
            if record_id in records_by_kind[kind]:
                report.error(f"data/{filename}: duplicate {kind} id {record_id!r}")
            records_by_kind[kind][record_id] = record
            record_locations[(kind, record_id)] = f"data/{filename}:{record_id}"

            errors = sorted(validator.iter_errors(record), key=lambda error: list(error.path))
            for error in errors:
                report.error(
                    f"data/{filename}:{record_id}:{json_path(error.path)}: {error.message}"
                )
            report.checked("Sample records")
            validate_review_provenance(filename, record, report)

    for kind, records in records_by_kind.items():
        for record_id, record in records.items():
            location = record_locations[(kind, record_id)]
            for target_kind, target_id, path in walk_references(record):
                target = records_by_kind.get(target_kind, {}).get(target_id)
                if target is None:
                    report.error(
                        f"{location}:{json_path(path)}: unknown {target_kind} id {target_id!r}"
                    )
                    continue
                report.checked("Cross-record references")

                if is_supported(record):
                    target_maturity = maturity_status(target)
                    target_review = review_status(target)
                    if target_maturity in DISALLOWED_DEPENDENCY_STATES or target_review in DISALLOWED_DEPENDENCY_STATES:
                        report.error(
                            f"{location}: supported record depends on {target_kind} {target_id!r} "
                            f"with maturity={target_maturity!r}, review={target_review!r}"
                        )
                    if target_kind == "source" and (
                        target_maturity != "supported" or target_review != "approved"
                    ):
                        report.error(
                            f"{location}: supported source-backed record depends on source {target_id!r} "
                            "that is not supported and approved"
                        )

            if is_supported(record) and review_status(record) != "approved":
                report.error(f"{location}: supported record must have approved review status")

            if kind == "legal_rule" and is_supported(record):
                statement = record.get("rule_statement", {})
                support = record.get("source_support", {})
                user_support = record.get("user_support", {})
                if statement.get("user_facing_allowed"):
                    if not support.get("required_source_ids"):
                        report.error(f"{location}: supported user-facing rule requires a source")
                    if not user_support.get("requires_citation"):
                        report.error(f"{location}: supported user-facing rule must require citation")

            if kind == "response" and is_supported(record):
                source_use = record.get("source_use", {})
                if source_use.get("source_required"):
                    allowed = set(source_use.get("allowed_source_review_statuses", []))
                    if allowed - {"reviewed", "approved"}:
                        report.error(
                            f"{location}: supported source-backed response allows non-reviewed source states"
                        )
                    high_risk = {"high", "extreme"}.intersection(
                        record.get("risk", {}).get("risk_levels_supported", [])
                    )
                    if high_risk and allowed != {"approved"}:
                        report.error(
                            f"{location}: high-risk supported response must allow only approved sources"
                        )

    validate_markdown(report)

    stale_patterns = {
        "old repository identity": re.compile("zeit" + "cow" + re.escape("/pro-one"), re.IGNORECASE),
        "PR-history wording": re.compile(r"\bThis PR " + "introduces" + r"\b", re.IGNORECASE),
    }
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in {".md", ".json", ".yml", ".yaml", ".py"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError as exc:
            report.error(f"{path.relative_to(ROOT)}: invalid UTF-8 text: {exc}")
            continue
        for label, pattern in stale_patterns.items():
            if pattern.search(text):
                report.error(f"{path.relative_to(ROOT)}: contains stale {label}")

    if report.errors:
        print(f"Repository validation failed with {len(report.errors)} error(s):", file=sys.stderr)
        for error in report.errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    summary = ", ".join(f"{name}: {count}" for name, count in sorted(report.counts.items()))
    print(f"Repository validation passed ({summary}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
