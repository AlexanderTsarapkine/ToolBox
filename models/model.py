from pydantic import BaseModel
from utilities.utilities import read_file
from agents.commentor import generate_comment
import typer


class Terminal(BaseModel):

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
            file_text = read_file(file)
            print(f"Read File: {file}")
            print("Generating Comment...")
            generate_comment(file_text)
            print("Done!")

        app()






