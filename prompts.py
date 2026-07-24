RESUME_ANALYSIS_PROMPT = """
You are an expert ATS Resume Reviewer.

Analyze the resume below.

Return ONLY valid JSON.

The JSON must follow this exact structure:

{{
    "ats_score": 0,
    "summary": "",
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "suggestions": []
}}

Resume:

{}
"""