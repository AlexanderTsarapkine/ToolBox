from typing import Tuple


def read_file(path:str) -> str:
    with open(path, 'r') as f:
        text = f.read()
        return text