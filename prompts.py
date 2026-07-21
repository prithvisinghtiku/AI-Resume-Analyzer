RESUME_ANALYSIS_PROMPT = """
You are a professional resume reviewer and ATS expert.

Analyze the following resume and provide:

1. Professional Summary
2. Strengths
3. Weaknesses
4. ATS Score (0-100)
5. Missing Skills
6. Suggestions for Improvement

Resume:

{}
"""