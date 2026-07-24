# AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An intelligent resume analysis application that leverages Google Gemini AI to evaluate resumes, estimate ATS compatibility, identify strengths and weaknesses, and provide actionable improvement suggestions through an interactive Streamlit interface.

Upload a PDF resume and receive instant AI-powered feedback including:

- 📄 Professional Summary
- ✅ Strengths
- ⚠️ Weaknesses
- 📊 ATS Score
- 🛠 Missing Skills
- 💡 Suggestions for Improvement

---

## Demo

*(Coming Soon)*

---

## Screenshots

### Upload Resume

(Add screenshot here)

### AI Analysis

(Add screenshot here)

---

## Tech Stack

- Python 3.14
- Streamlit
- Google Gemini API
- PyPDF2
- python-dotenv

---

## Project Structure

```text
ResumeAnalyzer/
│── app.py
│── ai.py
│── pdf_reader.py
│── prompts.py
│── requirements.txt
│── .gitignore
│── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/prithvisinghtiku/AI-Resume_Analyzer.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run

```bash
streamlit run app.py
```

---

## Features

✔ Upload PDF resumes

✔ Automatic PDF text extraction

✔ AI-powered resume evaluation

✔ ATS compatibility score

✔ Strengths & weaknesses detection

✔ Missing skills identification

✔ Personalized improvement suggestions

✔ Responsive Streamlit interface

---

## Future Improvements

- Resume vs Job Description Matching
- AI-powered Cover Letter Generator
- Resume Rewriting
- Export analysis as PDF
- Multi-language support
- User authentication
- Cloud deployment

---

## Author

**Prithvi Singh Tiku**

Built as part of my AI portfolio while learning Python and Generative AI.