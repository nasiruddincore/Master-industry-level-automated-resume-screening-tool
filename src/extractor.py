import pdfplumber
from docx import Document


def extract_pdf(file_path):

    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        print(f"PDF Error: {e}")

    return text


def extract_docx(file_path):

    text = ""

    try:
        doc = Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    except Exception as e:
        print(f"DOCX Error: {e}")

    return text


def extract_text(file_path):

    if file_path.endswith(".pdf"):
        return extract_pdf(file_path)

    elif file_path.endswith(".docx"):
        return extract_docx(file_path)

    return ""