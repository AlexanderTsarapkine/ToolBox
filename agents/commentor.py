import asyncio
import os 
from langchain.llms import OpenAI
from prompts.comment import COMMENT_CODE

LLM = OpenAI(
    temperature=0.9
    ) # type: ignore

def generate_comment(text: str):
    resp = LLM.generate(
        [COMMENT_CODE.format(code=text)]
    )   
    print(resp.generations[0][0].text)




