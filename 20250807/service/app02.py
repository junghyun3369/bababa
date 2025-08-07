from fastapi import Path, Form
from typing import Annotated

def get(txt : str):
  return {"result": txt}

def post(txt : Annotated[str, Form(...)]):
  return {"result": txt}

study02 = {
  "prefix":"/s2", 
  "tags":["연습2"],
  "urls" : [
    {
      "methods":["GET"], 
      "path":"/",
      "endpoint": get,
    },
    {
      "methods":["POST"], 
      "path":"/",
      "endpoint": post,
    },
  ]
}

