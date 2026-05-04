# Sample Web Application Pentest Finding Report

| Field | Value |
|---|---|
| Author | Owls Hippie || Date | 2026-05-04 || Report Type | PENTEST |

---

## 1. Executive Summary

A reflected cross-site scripting issue was identified in a demo web application search parameter. The application reflects user-controlled input in the HTTP response without sufficient output encoding.

**Key Risk:** An attacker may craft a malicious URL that executes JavaScript in the victim's browser when opened.

---

## 2. Target Information

| Field | Value |
|---|---|
| service | Demo Web Application |
| scope | Authorized lab environment |
| finding_id | WEB-001 |
| affected_endpoint | /search?q= |
| vulnerability_type | Reflected Cross-Site Scripting |
| cwe | CWE-79 |
| owasp_category | Injection |

---

## 3. Severity Assessment

| Field | Value |
|---|---|
| risk_level | Medium |
| impact | Session theft, phishing, or arbitrary script execution in the user's browser |
| likelihood | Medium |
| exploitability | User interaction may be required |

---

## 4. Technical Analysis

The affected endpoint reflects the q parameter into the response body. If the input is not properly encoded before rendering, browser-side script execution may occur.

---

## 5. Attack Flow

| Step | Description |
|---|---|
| 1 | The attacker identifies an input parameter reflected in the response. |
| 2 | The attacker crafts a URL containing a script payload. |
| 3 | The victim opens the crafted URL. |
| 4 | The script executes in the victim's browser context. |

---

## 6. Detection Points

### Application

- Review server logs for suspicious script-like payloads in query parameters.
- Monitor repeated requests containing encoded JavaScript patterns.

### Code

- Inspect output rendering logic for missing context-aware encoding.
- Verify whether template auto-escaping is enabled.


---

## 7. Indicators of Compromise

### Urls

- https://example.com/search?q=<sanitized-payload>

### Parameters

- q


---

## 8. MITRE ATT&CK Mapping

| Tactic | Technique ID | Technique Name | Evidence |
|---|---|---|---|
| Initial Access | T1189 | Drive-by Compromise | A crafted URL may be used to trigger browser-side script execution. |
| Credential Access | T1539 | Steal Web Session Cookie | In insecure configurations, script execution may be abused to access session-related data. |

---

## 9. Mitigation and Remediation

- Apply context-aware output encoding.
- Validate and sanitize user-controlled input.
- Enable Content Security Policy where appropriate.
- Use framework-provided template escaping features.
- Add automated security tests for reflected input handling.

---

## 10. References

- OWASP Web Security Testing Guide
- OWASP Cross Site Scripting Prevention Cheat Sheet
- CWE-79
