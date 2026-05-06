import re
from typing import Any


CVE_PATTERN = re.compile(r"^CVE-\d{4}-\d{4,}$", re.IGNORECASE)
ATTACK_TECHNIQUE_PATTERN = re.compile(r"^T\d{4}(?:\.\d{3})?$")
HEX_PATTERN = re.compile(r"^[a-fA-F0-9]+$")

VALID_RISK_LEVELS = {
    "informational",
    "info",
    "low",
    "medium",
    "high",
    "critical",
}

PLACEHOLDER_VALUES = {
    "",
    "sanitized",
    "redacted",
    "n/a",
    "na",
    "none",
    "to be verified",
    "unknown",
}


def _is_placeholder(value: Any) -> bool:
    return str(value).strip().lower() in PLACEHOLDER_VALUES


def validate_cve_id(cve_id: str) -> bool:
    return bool(CVE_PATTERN.match(cve_id.strip()))


def validate_attack_technique_id(technique_id: str) -> bool:
    return bool(ATTACK_TECHNIQUE_PATTERN.match(technique_id.strip()))


def validate_hash_value(hash_value: str) -> bool:
    """
    Accepts common hash lengths:
    - MD5: 32 hex chars
    - SHA1: 40 hex chars
    - SHA256: 64 hex chars

    Sanitized placeholders are allowed for public example reports.
    """

    value = hash_value.strip()

    if _is_placeholder(value):
        return True

    if len(value) not in {32, 40, 64}:
        return False

    return bool(HEX_PATTERN.match(value))


def validate_risk_level(risk_level: str) -> bool:
    return risk_level.strip().lower() in VALID_RISK_LEVELS


def validate_report_data(data: dict[str, Any]) -> None:
    """
    Validate report data after basic Pydantic schema validation.

    This function intentionally validates only security-relevant fields that
    benefit from strict format checks.
    """

    errors: list[str] = []

    report_type = data.get("report_type")
    target = data.get("target", {}) or {}
    severity = data.get("severity", {}) or {}
    iocs = data.get("iocs", {}) or {}
    attack_mapping = data.get("attack_mapping", []) or []

    if report_type == "cve":
        cve_id = target.get("cve_id")

        if not cve_id:
            errors.append("CVE report requires target.cve_id.")

        elif not validate_cve_id(str(cve_id)):
            errors.append(
                f"Invalid CVE ID: {cve_id}. Expected format: CVE-YYYY-NNNN."
            )

    risk_level = severity.get("risk_level")

    if risk_level and not validate_risk_level(str(risk_level)):
        errors.append(
            f"Invalid risk_level: {risk_level}. "
            "Allowed values: Informational, Low, Medium, High, Critical."
        )

    hashes = iocs.get("hashes", []) or []

    for hash_value in hashes:
        if not validate_hash_value(str(hash_value)):
            errors.append(
                f"Invalid hash value: {hash_value}. "
                "Expected MD5, SHA1, SHA256, or a sanitized placeholder."
            )

    for index, mapping in enumerate(attack_mapping, start=1):
        technique_id = mapping.get("technique_id")

        if technique_id and not validate_attack_technique_id(str(technique_id)):
            errors.append(
                f"Invalid ATT&CK technique_id at attack_mapping[{index}]: "
                f"{technique_id}. Expected format: T1234 or T1234.001."
            )

    if errors:
        message = "Report validation failed:\n" + "\n".join(
            f"- {error}" for error in errors
        )
        raise ValueError(message)