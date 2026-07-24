import streamlit as st

from pdf_reader import extract_text
from ai import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)
with st.sidebar:

    st.header("🤖 AI Resume Analyzer")

    st.write("Powered by Google Gemini")

    st.divider()

    st.write("### Features")

    st.write("✅ ATS Score")
    st.write("✅ Resume Summary")
    st.write("✅ Strengths")
    st.write("✅ Weaknesses")
    st.write("✅ Suggestions")

    st.divider()

    st.caption("Created by Prithvi Singh Tiku")


st.title("🤖 AI Resume Analyzer")
st.caption("Built with Python | Streamlit | Google Gemini AI")

st.markdown("""
Analyze your resume using **Google Gemini AI**.

Get:
- 📊 ATS Score
- ✅ Strengths
- ⚠️ Weaknesses
- 💡 Improvement Suggestions
""")

# Create two columns
left, right = st.columns([2, 1])

# Left column
with left:
    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"],
        help="Upload your resume in PDF format for an AI-Powered analysis."
    )

# Right column
with right:
    st.info("""
### Tips

✔ Upload a PDF

✔ Keep it clean

✔ Include your skills

✔ Include your experience
""")

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    with st.spinner("🤖 AI is analyzing your resume..."):
       try:
        analysis = analyze_resume(resume_text)
       except Exception as e:
        st.error(str(e))
        st.stop()
        st.divider()

    st.subheader("📊 ATS Score")

    st.metric(
    label="Score",
    value=f"{analysis['ats_score']}%"
    )

    st.subheader("📝 Professional Summary")
    st.write(analysis["summary"])

    st.subheader("✅ Strengths")

    for strength in analysis["strengths"]:
        st.write(f"• {strength}")

    st.subheader("⚠️ Weaknesses")

    for weakness in analysis["weaknesses"]:
        st.write(f"• {weakness}")

    st.subheader("📚 Missing Skills")

    for skill in analysis["missing_skills"]:
        st.write(f"• {skill}")

    st.subheader("💡 Suggestions")

    for suggestion in analysis["suggestions"]:
        st.write(f"• {suggestion}")