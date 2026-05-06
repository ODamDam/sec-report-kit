from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field
from sec_report_kit.validators import validate_report_data


class ReportInput(BaseModel):
    """
    Minimal report schema for sec-report-kit.

    The schema is intentionally flexible in v0.1.0.
    Additional fields are allowed so that CVE, malware, and pentest reports
    can evolve without breaking the renderer.
    """

    model_config = ConfigDict(extra="allow")

    report_type: Literal["cve", "malware", "pentest"]
    title: str
    author: str | None = None
    date: str | None = None

    target: dict[str, Any] = Field(default_factory=dict)
    severity: dict[str, Any] = Field(default_factory=dict)
    summary: dict[str, Any] = Field(default_factory=dict)
    attack_flow: list[dict[str, Any]] = Field(default_factory=list)
    detection: dict[str, Any] = Field(default_factory=dict)
    mitigation: list[str] = Field(default_factory=list)
    iocs: dict[str, Any] = Field(default_factory=dict)
    attack_mapping: list[dict[str, Any]] = Field(default_factory=list)
    rules: dict[str, Any] = Field(default_factory=dict)
    references: list[str] = Field(default_factory=list)


def load_report(path: Path) -> dict[str, Any]:
    """
    Load and validate a YAML report file.
    """

    if not path.exists():
        raise FileNotFoundError(f"Input file does not exist: {path}")

    with path.open("r", encoding="utf-8") as f:
        raw_data = yaml.safe_load(f)

    if raw_data is None:
        raise ValueError(f"Input file is empty: {path}")

    report = ReportInput.model_validate(raw_data)
    data = report.model_dump()

    validate_report_data(data)

    return data