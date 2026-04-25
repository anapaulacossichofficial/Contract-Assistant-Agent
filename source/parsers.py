import re
from datetime import datetime
from docx import Document
from pypdf import PdfReader


def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join([p.text for p in doc.paragraphs])

    elif uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text

    return ""


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def parse_money(text: str) -> float:
    match = re.search(r"r\$\s*([\d\.\,]+)", text, re.IGNORECASE)
    if match:
        value = match.group(1).replace(".", "").replace(",", ".")
        try:
            return float(value)
        except ValueError:
            return 0.0
    return 0.0


def parse_dates(text: str):
    date_matches = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)

    parsed_dates = []
    for d in date_matches:
        try:
            parsed_dates.append(datetime.strptime(d, "%d/%m/%Y"))
        except ValueError:
            pass

    if not parsed_dates:
        return None, None

    start_date = min(parsed_dates)
    end_date = max(parsed_dates)

    return start_date, end_date