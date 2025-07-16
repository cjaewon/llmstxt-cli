from typing import Annotated

import typer
from rich import print
from rich.console import Console

app = typer.Typer()
err_console = Console(stderr=True)

@app.command()
def gen():
  """Generate llms.txt or llms-full.txt from various source (file path, url ..)"""
  pass

@app.command()
def convert():
  """Convert llms.txt to llms-full.txt"""

if __name__ == "__main__":
  app()