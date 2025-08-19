import docx2txt
import pdfplumber
import tempfile

def extract_text_from_pdf(file) -> str:
    # Extract text from uploaded PDF file
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

def extract_text_from_docx(file) -> str:
    # Extract text from uploaded DOCX file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name
    return docx2txt.process(tmp_path).strip()

def parse_resume(uploaded_file) -> str:
    # Detects file type and extracts resume text
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword"
    ]:
        return extract_text_from_docx(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")