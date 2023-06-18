"""This file contains the Commentor model."""
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)


def comment_code() -> str:
    """Main function to comment code"""
    preprocess_code()

    
    
    return ""
    

def preprocess_code(path:str | None=None) -> str:
    """Preprocesses the code fro prompting"""

    # Load the code
    path = path or "./main.py"
    with open(path, "r") as f:
        code = f.read()

    # Split the code into chunks
    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=50, chunk_overlap=0
    )
    python_docs = python_splitter.create_documents([code])

    
    return ""