from typing import Annotated

import typer
from rich import print
from rich.console import Console

app = typer.Typer()

@app.command()
def convert(output: Annotated[str, typer.Option("--output", "-o")]):
  """Convert llms.txt to llms-full.txt"""
