from fastapi import Path, Form, File, UploadFile
from fastapi.responses import FileResponse
from typing import Annotated
import os
import shutil
import mimetypes
from uuid import uuid4

#저장 위치 설정 및 생성
UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def post(txt : Annotated[str, Form(...)], file : UploadFile = File(...)):
  
  # #파일 내용(이름,저장 경로) 이름. 확장명
  # fileName = file.filename
  ext = file.filename.split(".")[-1]
  fileName = f"{uuid4().hex}.{ext}"
  filePath = os.path.join(UPLOAD_DIR, fileName)
  # ./uploaded_images/test.png
  
  #파일 저장 부분
  with open(filePath, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)
  
  return {"result": txt, "filePath": filePath, "fileName":fileName}
  # return {"result": txt, "name": file.filename}

def read(fileName : str):
  filePath = os.path.join(UPLOAD_DIR, fileName)
  mediaType, _ = mimetypes.guess_type(filePath)
  headers = {
    "Content-Disposition":f"inline; filename='{fileName}'"
  }
  return FileResponse(path=filePath, media_type=mediaType, filename=fileName, headers=headers)
  # return FileResponse(path=filePath,media_type = "application/octet-stream",filename=fileName )
  # return {"result" : "read", "filename" : filename, "filPath":filePath}

def get(txt : str):
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
    {
      "methods":["GET"], 
      "path":"/read",
      "endpoint": read,
    },
  ]
}


