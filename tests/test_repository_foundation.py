from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
VALIDATOR_PATH = ROOT / "scripts" / "validate_repository.py"

spec = importlib.util.spec_from_file_location("repository_validator", VALIDATOR_PATH)
assert spec and spec.loader
repository_validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = repository_validator
spec.loader.exec_module(repository_validator)


class StandaloneSchemaTests(unittest.TestCase):
    def validate_with_standard_cli(self, schema_name: str, instance: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", encoding="utf-8", delete=False
        ) as instance_file:
            json.dump(instance, instance_file)
            instance_path = Path(instance_file.name)
        try:
            return subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "jsonschema",
                    str(SCHEMA_DIR / schema_name),
                    "--base-uri",
                    SCHEMA_DIR.as_uri() + "/",
                    "--instance",
                    str(instance_path),
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
        finally:
            instance_path.unlink(missing_ok=True)

    def test_domain_schema_resolves_common_schema_without_custom_registry(self) -> None:
        workflow = json.loads(
            (ROOT / "data" / "sample-workflows.json").read_text(encoding="utf-8")
        )[0]
        result = self.validate_with_standard_cli("workflow.schema.json", workflow)
        self.assertEqual(0, result.returncode, result.stderr)

    def test_supported_evaluation_fixture_requires_review_and_a_related_record(self) -> None:
        fixture = json.loads(
            (ROOT / "data" / "sample-evaluation-fixtures.json").read_text(encoding="utf-8")
        )[0]
        fixture["status"] = "supported"
        fixture["review"] = {
            "status": "approved",
            "reviewed_by": "schema-test-reviewer",
            "reviewer_role": "technical_reviewer",
            "review_scope": ["evaluation"],
            "reviewed_on": "2026-08-20",
            "reviewed_record_version": fixture["record_version"],
            "review_notes": "Synthetic test provenance; not sample-data review.",
        }

        valid_result = self.validate_with_standard_cli(
            "evaluation-fixture.schema.json", fixture
        )
        self.assertEqual(0, valid_result.returncode, valid_result.stderr)

        disconnected_fixture = copy.deepcopy(fixture)
        for field_name in disconnected_fixture["related_records"]:
            disconnected_fixture["related_records"][field_name] = []
        invalid_result = self.validate_with_standard_cli(
            "evaluation-fixture.schema.json", disconnected_fixture
        )
        self.assertNotEqual(0, invalid_result.returncode)


class CrossRecordReferenceTests(unittest.TestCase):
    def test_all_schema_reference_fields_have_explicit_specs(self) -> None:
        discovered: set[str] = set()
        for schema_path in SCHEMA_DIR.glob("*.json"):
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            discovered.update(
                repository_validator.discover_schema_reference_fields(schema)
            )
        self.assertEqual(discovered, set(repository_validator.REFERENCE_FIELDS))

    def test_typed_dangling_references_are_reported(self) -> None:
        record = {
            "status": "proposed",
            "review": {"status": "proposed"},
            "intake_ids": ["missing-intake"],
            "depends_on": ["missing-step"],
            "excluded_workflow_ids": ["missing-workflow"],
            "excluded_process_step_ids": ["missing-excluded-step"],
            "excluded_document_ids": ["missing-document"],
        }
        records = {"risk": {"fixture": record}}
        locations = {("risk", "fixture"): "test:fixture"}
        report = repository_validator.ValidationReport()

        repository_validator.validate_cross_record_references(
            records, locations, report
        )

        self.assertEqual(5, len(report.errors))
        self.assertTrue(all("unknown" in error for error in report.errors))

    def test_negative_fixture_source_may_be_rejected(self) -> None:
        fixture = {
            "status": "supported",
            "review": {"status": "approved"},
            "related_records": {"source_ids": ["rejected-source"]},
            "source_context": {
                "prohibited_source_ids": ["rejected-source"],
            },
        }
        rejected_source = {
            "status": "rejected",
            "review": {"status": "rejected"},
        }
        records = {
            "evaluation_fixture": {"fixture": fixture},
            "source": {"rejected-source": rejected_source},
        }
        locations = {
            ("evaluation_fixture", "fixture"): "test:fixture",
            ("source", "rejected-source"): "test:rejected-source",
        }
        report = repository_validator.ValidationReport()

        repository_validator.validate_cross_record_references(
            records, locations, report
        )

        self.assertEqual([], report.errors)

    def test_rejected_source_cannot_be_a_supporting_dependency(self) -> None:
        response = {
            "status": "supported",
            "review": {"status": "approved"},
            "related_records": {"source_ids": ["rejected-source"]},
            "source_use": {"source_required": False},
        }
        rejected_source = {
            "status": "rejected",
            "review": {"status": "rejected"},
        }
        records = {
            "response": {"response": response},
            "source": {"rejected-source": rejected_source},
        }
        locations = {
            ("response", "response"): "test:response",
            ("source", "rejected-source"): "test:rejected-source",
        }
        report = repository_validator.ValidationReport()

        repository_validator.validate_cross_record_references(
            records, locations, report
        )

        self.assertTrue(
            any("not supported and approved" in error for error in report.errors)
        )


class ProjectScanTests(unittest.TestCase):
    def test_generated_environment_directories_are_excluded(self) -> None:
        excluded_examples = (
            ROOT / ".venv" / "invalid.json",
            ROOT / "node_modules" / "invalid.md",
            ROOT / "vendor" / "invalid.yml",
            ROOT / "build" / "invalid.py",
        )
        self.assertTrue(
            all(not repository_validator.is_project_owned(path) for path in excluded_examples)
        )


if __name__ == "__main__":
    unittest.main()
