from pathlib import Path
from typing import List

import typer
from rich.console import Console

from sec_report_kit.renderer import render_report


app = typer.Typer(
    help="Generate security analysis reports from YAML input files."
)

console = Console()


@app.command()
def generate(
    input_file: Path = typer.Argument(
        ...,
        help="Path to the YAML report input file.",
    ),
    output_dir: Path = typer.Option(
        Path("outputs"),
        "--out",
        "-o",
        help="Directory where generated reports will be saved.",
    ),
    formats: List[str] = typer.Option(
        ["md", "html"],
        "--format",
        "-f",
        help="Output format. Supported values: md, html",
    ),
):
    """
    Generate a security analysis report.
    """

    try:
        generated_files = render_report(
            input_path=input_file,
            output_dir=output_dir,
            formats=formats,
        )

        console.print("[bold green]Report generation completed.[/bold green]")

        for file_path in generated_files:
            console.print(f"- {file_path}")

    except Exception as e:
        console.print("[bold red]Report generation failed.[/bold red]")
        console.print(str(e))
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()