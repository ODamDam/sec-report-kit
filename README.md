# sec-report-kit

`sec-report-kit` is a lightweight CLI tool for generating security analysis reports from structured YAML input files.

The project is designed for CVE analysis, malware triage, and penetration testing report workflows.  
It converts structured analysis data into Markdown and HTML reports.

## Features

- Generate security reports from YAML
- Support Markdown and HTML output
- Provide reusable report templates
- Structure CVE analysis reports
- Include detection points, IOC sections, mitigation guidance, and MITRE ATT&CK mapping

## Why I Built This

During malware triage and CVE analysis studies, report formats often became inconsistent and important sections such as IOC, ATT&CK mapping, detection points, and mitigation guidance were easy to omit.

This project standardizes the report writing process by separating structured analysis data from report presentation.

## Project Structure

```text
sec-report-kit/
├─ examples/
├─ outputs/
├─ templates/
└─ sec_report_kit/

## Example Reports

The repository includes generated sample reports under `examples/outputs/`.

| Report Type | Input YAML | Markdown | HTML |
|---|---|---|---|
| CVE Analysis | [cve-2023-38831.yaml](examples/cve/cve-2023-38831.yaml) | [Markdown](examples/outputs/cve-2023-38831.md) | [HTML](examples/outputs/cve-2023-38831.html) |
| Malware Triage | [agent-tesla-triage.yaml](examples/malware/agent-tesla-triage.yaml) | [Markdown](examples/outputs/agent-tesla-malware-triage-report.md) | [HTML](examples/outputs/agent-tesla-malware-triage-report.html) |