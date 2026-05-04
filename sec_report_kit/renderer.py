import re
from pathlib import Path
from typing import Iterable

from jinja2 import Environment, FileSystemLoader

from sec_report_kit.schema import load_report


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = PROJECT_ROOT / "templates"


def slugify(text: str) -> str:
    """
    Convert a report title or ID into a filesystem-friendly name.
    Unicode word characters are preserved.
    """

    text = text.strip().lower()
    text = re.sub(r"[^\w.-]+", "-", text, flags=re.UNICODE)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")

    return text or "security-report"


def get_report_slug(data: dict) -> str:
    target = data.get("target", {})

    candidate = (
        target.get("cve_id")
        or target.get("sample_name")
        or target.get("service")
        or data.get("title")
        or "security-report"
    )

    return slugify(str(candidate))


def build_environment() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_report(
    input_path: Path,
    output_dir: Path,
    formats: Iterable[str],
) -> list[Path]:
    """
    Render a report from YAML into selected output formats.
    Supported formats: md, html
    """

    data = load_report(input_path)

    output_dir.mkdir(parents=True, exist_ok=True)

    env = build_environment()
    slug = get_report_slug(data)

    generated_files: list[Path] = []

    for output_format in formats:
        output_format = output_format.lower()

        if output_format == "md":
            template = env.get_template("base.md.j2")
            output_path = output_dir / f"{slug}.md"

        elif output_format == "html":
            template = env.get_template("base.html.j2")
            output_path = output_dir / f"{slug}.html"

        else:
            raise ValueError(f"Unsupported output format: {output_format}")

        rendered = template.render(report=data)

        with output_path.open("w", encoding="utf-8") as f:
            f.write(rendered)

        generated_files.append(output_path)

    return generated_files