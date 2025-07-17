from fastapi import FastAPI , File , UploadFile

app = FastAPI()

@app.post('/uplaod')
async def upload_file(file : UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "content_type": file.content_type}
