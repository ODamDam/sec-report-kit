# YAML Schema

`sec-report-kit` uses YAML files as structured input for security analysis reports.

The schema is intentionally lightweight and flexible in the initial version.  
Each report type shares common fields, while allowing report-specific fields to evolve over time.

## Common Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `report_type` | string | Yes | Report type. Supported values: `cve`, `malware`, `pentest` |
| `title` | string | Yes | Report title |
| `author` | string | No | Report author |
| `date` | string | No | Report date |
| `target` | object | No | Target product, malware family, service, endpoint, or affected component |
| `severity` | object | No | Severity, risk level, CVSS, impact, likelihood, or confidence |
| `summary` | object | No | Executive summary, key risk, and technical details |
| `attack_flow` | list | No | Step-by-step attack, exploitation, infection, or abuse flow |
| `detection` | object | No | Host, network, log, application, or code-based detection points |
| `iocs` | object | No | Indicators of compromise such as hashes, domains, IPs, URLs, and file paths |
| `attack_mapping` | list | No | MITRE ATT&CK mapping information |
| `rules` | object | No | Detection rule references such as YARA and Sigma |
| `mitigation` | list | No | Mitigation and remediation guidance |
| `references` | list | No | External references |

## report_type

Supported values:

```yaml
report_type: cve
report_type: malware
report_type: pentest
```

## target

The target object describes the subject of the report.

## CVE Example
```
target:
  cve_id: "CVE-2023-38831"
  product: "WinRAR"
  vendor: "RARLAB"
  affected_versions: "WinRAR versions before 6.23"
  vulnerability_type: "Archive file processing vulnerability"
  impact: "Arbitrary code execution"
```

## Malware Example
```
target:
  malware_family: "Agent Tesla"
  file_type: "PE32 .NET executable"
  platform: "Windows"
  analysis_type: "Static and network-based triage"
```

## Pentest Example
```
target:
  service: "Demo Web Application"
  scope: "Authorized lab environment"
  finding_id: "WEB-001"
  affected_endpoint: "/search?q="
  vulnerability_type: "Reflected Cross-Site Scripting"
```

## severity
The severity object describes impact and risk.
```
severity:
  risk_level: "High"
  impact: "Credential theft and data exfiltration"
  confidence: "Medium"
```
For CVE reports, this section may include CVSS information.
```
severity:
  cvss_score: "7.8"
  cvss_vector: "CVSS:3.1/..."
  risk_level: "High"
  exploited_in_the_wild: true
```

## summary
The summary object contains the main narrative sections.
```
summary:
  overview: "Short overview of the issue."
  key_risk: "Main security risk."
  technical_details: "Technical explanation of the issue."
```

## attack_flow
The attack_flow field describes the sequence of attacker or malware behavior.
```
attack_flow:
  - step: 1
    description: "The attacker prepares a malicious file."
  - step: 2
    description: "The victim opens the file."
  - step: 3
    description: "The payload executes."
```

## detection

Detection points can be organized by category.
```
detection:
  host:
    - "Monitor suspicious child processes."
  network:
    - "Check abnormal outbound connections."
  log:
    - "Correlate process creation and network events."
```

## iocs
IOC categories are flexible.
```
iocs:
  hashes:
    - "sanitized"
  domains:
    - "example-c2[.]com"
  ips:
    - "192.0.2.10"
  file_paths:
    - "%APPDATA%\\sample.exe"
```

## attack_mapping
MITRE ATT&CK mapping entries use tactic, technique ID, technique name, and evidence.
```
attack_mapping:
  - tactic: "Execution"
    technique_id: "T1204.002"
    technique_name: "User Execution: Malicious File"
    evidence: "The infection flow depends on the user executing a malicious file."
```

## rules

The `rules` object links detection rule files to the generated report.

```yaml
rules:
  yara:
    - name: "agent_tesla_triage.yar"
      path: "rules/yara/agent_tesla_triage.yar"
      description: "Sample YARA rule for triage-level malware detection."
  sigma:
    - name: "suspicious_archive_child_process.yml"
      path: "rules/sigma/suspicious_archive_child_process.yml"
      description: "Sample Sigma rule for suspicious child processes spawned by archive utilities."
```
The current version links rule files in the report.
It does not validate the syntax of YARA or Sigma rules yet.

## mitigation
```
mitigation:
  - "Update affected software."
  - "Monitor suspicious process behavior."
  - "Apply endpoint protection policies."
```

## references
```
references:
  - "NVD"
  - "MITRE ATT&CK"
  - "Vendor advisory"
```

## Notes
- Do not include real malware binaries.
- Defang suspicious domains and URLs when publishing public examples.
- Do not include credentials, victim data, private IP ranges from real environments, or sensitive infrastructure details.
- Public examples should be sanitized.