from pathlib import Path

from sec_report_kit.renderer import render_report


def test_render_markdown_html_and_docx(tmp_path):
    input_path = Path("examples/cve/cve-2023-38831.yaml")

    generated_files = render_report(
        input_path=input_path,
        output_dir=tmp_path,
        formats=["md", "html", "docx"],
    )

    generated_suffixes = {path.suffix for path in generated_files}

    assert ".md" in generated_suffixes
    assert ".html" in generated_suffixes
    assert ".docx" in generated_suffixes

    for path in generated_files:
        assert path.exists()
        assert path.stat().st_size > 0


def test_render_html_contains_report_title(tmp_path):
    input_path = Path("examples/malware/agent-tesla-triage.yaml")

    generated_files = render_report(
        input_path=input_path,
        output_dir=tmp_path,
        formats=["html"],
    )

    html_path = generated_files[0]
    html_content = html_path.read_text(encoding="utf-8")

    assert "Agent Tesla" in html_content
    assert "Detection Rules" in html_content