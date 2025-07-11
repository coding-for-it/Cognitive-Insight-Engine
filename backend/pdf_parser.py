import pdfplumber

def extract_text_from_pdf(path):
    with pdfplumber.open(path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text
