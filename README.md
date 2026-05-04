# sec-report-kit

`sec-report-kit` is a lightweight CLI tool for generating security analysis reports from structured YAML input files.

`sec-report-kit`은 CVE 분석, 악성코드 트리아지, 모의해킹 Finding을 YAML로 구조화하고, 이를 Markdown/HTML 보고서로 자동 생성하는 보안 분석 보고서 자동화 도구입니다.

The project is designed for CVE analysis, malware triage, and penetration testing report workflows.  
It converts structured analysis data into Markdown and HTML reports.

## Overview

Security analysis reports often require repeated sections such as executive summary, target information, severity, technical analysis, attack flow, detection points, IOC, MITRE ATT&CK mapping, mitigation, and references.

This project separates structured analysis data from report presentation. Analysts write findings in YAML, and the tool generates consistent reports in Markdown and HTML.


## Supported Report Types

| Report Type | Description |
|---|---|
| CVE Analysis | Vulnerability analysis report for CVE-based research |
| Malware Triage | Malware triage report with IOC, behavior, and ATT&CK mapping |
| Pentest Finding | Penetration testing finding report for web or system vulnerabilities |

## Features

- YAML-based report input
- Markdown report generation
- HTML report generation
- Reusable report templates
- CVE analysis report example
- Malware triage report example
- Pentest finding report example
- IOC section support
- MITRE ATT&CK mapping section support
- Detection and mitigation sections
- YARA rule reference section
- Sigma rule reference section

## Project Structure

```text
sec-report-kit/
├─ docs/
│  └─ schema.md
├─ examples/
│  ├─ cve/
│  ├─ malware/
│  ├─ pentest/
│  └─ outputs/
├─ outputs/
├─ sec_report_kit/
├─ templates/
├─ README.md
├─ requirements.txt
├─ pyproject.toml
└─ LICENSE
```

## Installation
```git clone https://github.com/YOUR_USERNAME/sec-report-kit.git
cd sec-report-kit
```
```
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
```
python -m pip install --upgrade pip
```
```
python -m pip install -r requirements.txt
```

## Usage
Generate a report from a YAML input file:
```
python -m sec_report_kit.cli examples/cve/cve-2023-38831.yaml
```

Generate reports into examples/outputs:
```
python -m sec_report_kit.cli examples/cve/cve-2023-38831.yaml -o examples/outputs
python -m sec_report_kit.cli examples/malware/agent-tesla-triage.yaml -o examples/outputs
python -m sec_report_kit.cli examples/pentest/sample-web-finding.yaml -o examples/outputs
```
Generate only HTML:
```
python -m sec_report_kit.cli examples/cve/cve-2023-38831.yaml -f html
```
Generate only Markdown:
```
python -m sec_report_kit.cli examples/cve/cve-2023-38831.yaml -f md
```

YAML Schema

See docs/schema.md
.

## Roadmap
 - [x] YAML-based report input
 - [x] Markdown report generation
 - [x] HTML report generation
 - [x] CVE analysis report example
 - [x] Malware triage report example
 - [x] Pentest finding report example
 - [x] Example generated reports
 - [x] GitHub Pages demo
 - [x] YARA rule section
 - [x] Sigma rule section
 - [ ] DOCX export
 - [ ] PDF export
 - [ ] Input validation tests
 - [ ] Unit tests
- [ ] Disclaimer

This project is intended for educational and defensive security purposes only.

No malware binaries, live exploit code, real victim data, credentials, or sensitive infrastructure information are included in this repository.

## License

This project is licensed under the MIT License.