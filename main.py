from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
from pymongo import MongoClient
from resume_parser import extract_text_from_pdf
from model import parse_resume

#Initialize fast API
app = FastAPI()

#Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client.resumeDB
collection = db.resumes

#Upload resume
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = extract_text(file_path)
    analysis = analyze_resume(text)
    resume_data = {"filename": file.filename, "content": text, "analysis": analysis}
    return {"message": "Resume uploaded successfully", "data": analysis}

@app.get("/resumes/")
async def get_resumes():
    resumes = list(collection.find({},{"_id":0}))
    return {"resumes": resumes}