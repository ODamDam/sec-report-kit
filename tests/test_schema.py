from pathlib import Path

import pytest
import yaml

from sec_report_kit.schema import load_report


def write_yaml(tmp_path, data: dict) -> Path:
    path = tmp_path / "test-report.yaml"

    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True)

    return path


def test_valid_cve_report_loads():
    data = load_report(Path("examples/cve/cve-2023-38831.yaml"))

    assert data["report_type"] == "cve"
    assert data["title"]


def test_invalid_report_type_is_rejected(tmp_path):
    path = write_yaml(
        tmp_path,
        {
            "report_type": "invalid",
            "title": "Invalid Report",
        },
    )

    with pytest.raises(Exception):
        load_report(path)


def test_invalid_cve_id_is_rejected(tmp_path):
    path = write_yaml(
        tmp_path,
        {
            "report_type": "cve",
            "title": "Invalid CVE Report",
            "target": {
                "cve_id": "CVE-23-1",
            },
        },
    )

    with pytest.raises(ValueError, match="Invalid CVE ID"):
        load_report(path)


def test_invalid_attack_technique_id_is_rejected(tmp_path):
    path = write_yaml(
        tmp_path,
        {
            "report_type": "malware",
            "title": "Invalid ATT&CK Mapping Report",
            "attack_mapping": [
                {
                    "tactic": "Execution",
                    "technique_id": "INVALID-1204",
                    "technique_name": "Invalid Technique",
                    "evidence": "Test evidence",
                }
            ],
        },
    )

    with pytest.raises(ValueError, match="Invalid ATT&CK technique_id"):
        load_report(path)


def test_invalid_hash_is_rejected(tmp_path):
    path = write_yaml(
        tmp_path,
        {
            "report_type": "malware",
            "title": "Invalid Hash Report",
            "iocs": {
                "hashes": [
                    "not-a-valid-hash",
                ]
            },
        },
    )

    with pytest.raises(ValueError, match="Invalid hash value"):
        load_report(path)


def test_sanitized_hash_placeholder_is_allowed(tmp_path):
    path = write_yaml(
        tmp_path,
        {
            "report_type": "malware",
            "title": "Sanitized Hash Report",
            "iocs": {
                "hashes": [
                    "sanitized",
                ]
            },
        },
    )

    data = load_report(path)

    assert data["iocs"]["hashes"] == ["sanitized"]