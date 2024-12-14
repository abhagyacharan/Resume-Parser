from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from utils.resume_parser import extract_text_from_image
from utils.langchain_handler import categorize_resume
from db.db_setup import get_db
from db.models import save_to_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/upload/resume/")
async def upload_resume(file: UploadFile = File(...)):

    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as f:
        f.write(file.file.read())

    # Extract text from image
    extracted_text = extract_text_from_image(temp_file)

    # Categorize text using LLM
    categorized_data = categorize_resume(extracted_text)

    # Save to database
    with get_db() as db:
        save_to_db(db, categorized_data)


    return JSONResponse(content=categorized_data)