from pydantic import BaseModel
from utilities.utilities import read_file
from agents.commentor import generate_comment

class Terminal(BaseModel):

    @staticmethod
    def run():
        file_name = input("Enter file name: ")
        file_text = read_file(file_name)
        print(f"Read File: {file_name}")

        print("Generating Comment...")
        generate_comment(file_text)
        print("Done!")





