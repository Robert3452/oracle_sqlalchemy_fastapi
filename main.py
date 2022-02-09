from routes.user import user
from routes.product import router
from typing import List

from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

app.include_router(user)
app.include_router(router)


@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
