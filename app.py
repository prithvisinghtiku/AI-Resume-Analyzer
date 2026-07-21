import streamlit as st

from pdf_reader import extract_text
from ai import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and let AI analyze it.")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    with st.spinner("🤖 AI is analyzing your resume..."):
        analysis = analyze_resume(resume_text)
    st.success("✅ Resume uploaded successfully!")

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Contents",
        resume_text,
        height=400
    )

    st.subheader("🤖 AI Analysis")

    st.write(analysis)