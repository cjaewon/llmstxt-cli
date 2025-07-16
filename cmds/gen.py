from typing import Annotated

import typer
from rich import print
from rich.console import Console

app = typer.Typer()

@app.command()
def gen(
  sources: Annotated[list[str], typer.Argument()],
  output: Annotated[str, typer.Option("--output", "-o")],
  full: Annotated[bool, typer.Option("--full", "-f", help="Generate in the extended 'llms-full.txt' format")] = False,
):
  """Generate llms.txt or llms-full.txt from various source (file path, url ..)"""
  pass
