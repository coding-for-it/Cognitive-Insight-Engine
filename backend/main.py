from fastapi import FastAPI, UploadFile, File
from backend.pdf_parser import extract_text_from_pdf
from backend.preprocess import clean_text, extract_sections
from backend.kpi_extractor import extract_kpis
from backend.sentiment import analyze_sentiment
import pandas as pd
import tempfile

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    suffix = file.filename.split('.')[-1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix='.' + suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    if suffix == "pdf":
        text = extract_text_from_pdf(tmp_path)
    elif suffix == "xlsx":
        df = pd.read_excel(tmp_path)
        text = "\n".join(df.astype(str).apply(" ".join, axis=1))  # Convert rows to text
    else:
        return {"error": "Unsupported file type"}

    cleaned_text = clean_text(text)
    sections = extract_sections(cleaned_text)
    kpis = extract_kpis(cleaned_text)
    sentiment = analyze_sentiment(cleaned_text)

    return {
        "kpis": kpis,
        "sentiment": sentiment,
        "sections": list(sections.keys())
    }
