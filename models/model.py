from pydantic import BaseModel
from utilities.utilities import read_file

class Terminal(BaseModel):

    def run(self):
        file_name = input("Enter file name: ")
        file_text = read_file(file_name)
        print(f"File text: {file_text}")




