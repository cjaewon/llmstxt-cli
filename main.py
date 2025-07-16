from typing import Annotated

import typer
from rich import print
from rich.console import Console

from cmds import gen, convert

app = typer.Typer()
err_console = Console(stderr=True)

app.add_typer(gen.app)
app.add_typer(convert.app)

if __name__ == "__main__":
  app()
