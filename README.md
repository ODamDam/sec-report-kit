# sec-report-kit

**sec-report-kit** is a lightweight CLI tool for generating security analysis reports from structured YAML input files.

sec-report-kit은 CVE 분석, 악성코드 트리아지, 모의해킹 Finding을 YAML로 구조화하고, 이를 Markdown, HTML, DOCX 보고서로 자동 생성하는 보안 분석 보고서 자동화 도구이다.

The project is designed for CVE analysis, malware triage, and penetration testing report workflows.

It separates structured security analysis data from report presentation and converts YAML-based findings into consistent, reusable report formats.

---

## Overview

Security analysis reports often require repeated sections such as:

* Executive summary
* Target information
* Severity
* Technical analysis
* Attack flow
* Detection points
* IOC
* MITRE ATT&CK mapping
* Mitigation
* References

This project separates structured analysis data from report presentation.

Analysts write findings in YAML, and the tool generates consistent reports in Markdown, HTML, and DOCX formats.

---

## Supported Report Types

| Report Type     | Description                                                          |
| --------------- | -------------------------------------------------------------------- |
| CVE Analysis    | Vulnerability analysis report for CVE-based research                 |
| Malware Triage  | Malware triage report with IOC, behavior, and ATT&CK mapping         |
| Pentest Finding | Penetration testing finding report for web or system vulnerabilities |

---

## Features

* YAML-based report input
* Markdown report generation
* HTML report generation
* DOCX report generation
* Reusable report templates
* CVE analysis report workflow
* Malware triage report workflow
* Pentest finding report workflow
* IOC section support
* MITRE ATT&CK mapping section support
* Detection and mitigation sections
* YARA rule reference section
* Sigma rule reference section
* Security-focused input validation
* Unit tests for schema loading and report rendering
* GitHub Pages demo report publishing
* Automatic GitHub Pages index generation from generated HTML reports

---

## GitHub Pages Demo

This repository includes a GitHub Pages demo site for viewing generated HTML reports.

The demo page lists generated reports from the `docs/reports/` directory and links each HTML report from `docs/index.html`.

Example report categories include:

* CVE Analysis
* Malware Triage
* Pentest Finding

Generated HTML reports can be copied into `docs/reports/`.

Then the GitHub Pages index can be regenerated using:

* PowerShell: `python scripts\build_index.py`

This command scans `docs/reports/*.html` and rebuilds `docs/index.html` automatically.

---

## Example Reports

Current example workflows include:

| Type            | Example                                                 |
| --------------- | ------------------------------------------------------- |
| CVE Analysis    | CVE-2023-38831 WinRAR Vulnerability Report              |
| CVE Analysis    | CVE-2021-41773 Apache HTTP Server Path Traversal Report |
| Malware Triage  | Agent Tesla Malware Triage Report                       |
| Pentest Finding | Sample Web Application Pentest Finding Report           |

The CVE-2021-41773 report includes a local Docker-based verification of Apache HTTP Server 2.4.49 path traversal behavior, access log review, mitigation validation, and Sigma-style detection logic.

---

## Project Structure

* `sec-report-kit/`

  * `docs/`

    * `index.html`
    * `schema.md`
    * `reports/`

      * `cve-2023-38831.html`
      * `cve-2021-41773-*.html`
      * `agent-tesla-malware-triage-report.html`
      * `demo-web-application.html`
  * `examples/`

    * `cve/`

      * `cve-2023-38831.yaml`
      * `cve-2021-41773.yaml`
    * `malware/`
    * `pentest/`
    * `outputs/`
  * `outputs/`
  * `scripts/`

    * `build_index.py`
  * `sec_report_kit/`
  * `templates/`
  * `tests/`
  * `README.md`
  * `requirements.txt`
  * `pyproject.toml`
  * `LICENSE`

---

## Installation

1. Move into the project directory.

   `cd sec-report-kit`

2. Create a virtual environment.

   `python -m venv .venv`

3. Allow script execution for the current PowerShell process.

   `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

4. Activate the virtual environment.

   `.\.venv\Scripts\Activate.ps1`

5. Upgrade pip.

   `python -m pip install --upgrade pip`

6. Install dependencies.

   `python -m pip install -r requirements.txt`

7. Optional: install the project in editable mode.

   `python -m pip install -e .`

---

## Usage

### Generate a report from a YAML input file

`python -m sec_report_kit.cli examples/cve/cve-2023-38831.yaml`

### Generate reports into `examples/outputs`

* CVE report: `python -m sec_report_kit.cli examples/cve/cve-2023-38831.yaml -o examples/outputs`
* CVE report: `python -m sec_report_kit.cli examples/cve/cve-2021-41773.yaml -o examples/outputs`
* Malware triage report: `python -m sec_report_kit.cli examples/malware/agent-tesla-triage.yaml -o examples/outputs`
* Pentest finding report: `python -m sec_report_kit.cli examples/pentest/sample-web-finding.yaml -o examples/outputs`

### Generate Markdown, HTML, and DOCX together

`python -m sec_report_kit.cli examples/cve/cve-2021-41773.yaml -o examples/outputs -f md -f html -f docx`

### Generate only HTML

`python -m sec_report_kit.cli examples/cve/cve-2023-38831.yaml -f html`

### Generate only Markdown

`python -m sec_report_kit.cli examples/cve/cve-2023-38831.yaml -f md`

### Generate only DOCX

`python -m sec_report_kit.cli examples/cve/cve-2023-38831.yaml -f docx`

---

## Publishing Reports to GitHub Pages

After generating an HTML report, copy the generated HTML file into `docs/reports/`.

Example:

`copy examples\outputs\cve-2021-41773-*.html docs\reports\`

Then regenerate the GitHub Pages index:

`python scripts\build_index.py`

Commit and push the updated files:

1. `git add .`
2. `git commit -m "Add CVE-2021-41773 report to GitHub Pages"`
3. `git push origin main`

The GitHub Pages demo page will then include the newly generated HTML report.

---

## YAML Schema

See `docs/schema.md`.

---

## Roadmap

* [x] YAML-based report input
* [x] Markdown report generation
* [x] HTML report generation
* [x] DOCX export
* [x] CVE analysis report example
* [x] Malware triage report example
* [x] Pentest finding report example
* [x] Example generated reports
* [x] GitHub Pages demo
* [x] Automatic GitHub Pages index generation
* [x] YARA rule section
* [x] Sigma rule section
* [x] Input validation tests
* [x] Unit tests
* [ ] More report templates
* [ ] More detection rule export formats
* [ ] Additional security report examples

---

## Disclaimer

This project is intended for educational and defensive security purposes only.

No malware binaries, live exploit code, real victim data, credentials, or sensitive infrastructure information are included in this repository.

The included reports and examples are designed for safe local verification, documentation practice, and defensive security analysis workflows.

---

## License

This project is licensed under the MIT License.
