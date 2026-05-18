from pathlib import Path
import re
from html import escape

DOCS_DIR = Path("docs")
REPORTS_DIR = DOCS_DIR / "reports"
INDEX_PATH = DOCS_DIR / "index.html"


def title_from_filename(path: Path) -> str:
    name = path.stem
    name = name.replace("-", " ").replace("_", " ")
    name = re.sub(r"\s+", " ", name).strip()
    return name.title()


def infer_badge(filename: str) -> str:
    lower = filename.lower()

    if "cve" in lower:
        return "CVE Analysis"
    if "malware" in lower or "triage" in lower:
        return "Malware Triage"
    if "pentest" in lower or "web-application" in lower:
        return "Pentest Finding"

    return "Security Report"


def infer_description(filename: str) -> str:
    lower = filename.lower()

    if "cve" in lower:
        return "Generated report for a CVE-based vulnerability analysis workflow."
    if "malware" in lower or "triage" in lower:
        return "Generated report for malware triage, IOC organization, and ATT&CK mapping."
    if "pentest" in lower or "web-application" in lower:
        return "Generated report for penetration testing finding documentation."

    return "Generated security analysis report."


def sort_key(path: Path):
    lower = path.name.lower()

    if "cve-2021-41773" in lower:
        return (0, lower)
    if "cve" in lower:
        return (1, lower)
    if "malware" in lower or "triage" in lower:
        return (2, lower)
    if "pentest" in lower or "web-application" in lower:
        return (3, lower)

    return (9, lower)


def build_cards() -> str:
    html_files = sorted(REPORTS_DIR.glob("*.html"), key=sort_key)

    cards = []
    for report in html_files:
        title = title_from_filename(report)
        badge = infer_badge(report.name)
        description = infer_description(report.name)
        href = f"reports/{report.name}"

        cards.append(f"""
  <div class="card">
    <span class="badge">{escape(badge)}</span>
    <h2>{escape(title)}</h2>
    <p>
      {escape(description)}
    </p>
    <a href="{escape(href)}">View HTML Report</a>
  </div>
""")

    return "\n".join(cards)


def main():
    if not REPORTS_DIR.exists():
        raise FileNotFoundError(f"Reports directory not found: {REPORTS_DIR}")

    cards = build_cards()

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>sec-report-kit Demo Reports</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 40px;
      background-color: #f7f7f7;
      color: #222;
    }}

    .container {{
      max-width: 960px;
      margin: 0 auto;
      background: #fff;
      padding: 40px;
      border-radius: 12px;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
    }}

    h1 {{
      border-bottom: 3px solid #222;
      padding-bottom: 12px;
    }}

    .card {{
      border: 1px solid #ddd;
      border-radius: 10px;
      padding: 20px;
      margin: 16px 0;
      background: #fafafa;
    }}

    .card h2 {{
      margin-top: 0;
    }}

    a {{
      color: #0645ad;
      font-weight: bold;
      text-decoration: none;
    }}

    a:hover {{
      text-decoration: underline;
    }}

    .badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 999px;
      background-color: #222;
      color: #fff;
      font-size: 0.8rem;
      font-weight: bold;
    }}

    .muted {{
      color: #666;
    }}
  </style>
</head>
<body>
<div class="container">
  <h1>sec-report-kit Demo Reports</h1>

  <p>
    <strong>sec-report-kit</strong> is a lightweight CLI tool that converts
    structured YAML-based security analysis data into consistent Markdown and HTML reports.
  </p>

  <p class="muted">
    This page provides generated sample reports for CVE analysis, malware triage,
    and penetration testing finding workflows.
  </p>

{cards}

  <hr>

  <p class="muted">
    Educational and defensive security use only. No malware binaries, live exploit code,
    or sensitive victim data are included.
  </p>
</div>
</body>
</html>
"""

    INDEX_PATH.write_text(index_html, encoding="utf-8")
    print(f"Generated {INDEX_PATH}")
    print(f"Linked {len(list(REPORTS_DIR.glob('*.html')))} HTML reports.")


if __name__ == "__main__":
    main()