from pydantic import BaseModel
from utilities.utilities import read_file
import typer
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn
import time # Can remove only used for fake delay

class Terminal(BaseModel):
    """Terminal class for handling all terminal commands"""

    @staticmethod
    def run():
        app = typer.Typer()
        commentor_app = typer.Typer()
        # pr_app = typer.Typer()

        app.add_typer(commentor_app, name="comment")

        @commentor_app.command("all")
        def comment_all(root: str):
            # do stuff to comment everything starting from root
            pass
            
        @commentor_app.command("single")
        def comment_single(file: str):

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description=f"[green]Reading {file}...[/green]", total=None)
                file_text = read_file(file)
                time.sleep(3) # fake delay to see animation

            print(f"[yellow]Read File: {file}[/yellow]")

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description="[green]Generating Comments...[/green]", total=None)


                time.sleep(3)

            print("[magenta]Done![/magenta]")

        app()




