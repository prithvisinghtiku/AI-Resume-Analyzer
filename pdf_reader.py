from PyPDF2 import PdfReader


def extract_text(uploaded_file):
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text

    return resume_text