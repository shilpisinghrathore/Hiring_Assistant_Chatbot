# prompts.py

def technical_questions_prompt(tech: str) -> str:
    return f"""
You are an expert technical interviewer.

Given a technology or topic: "{tech}"

Please generate exactly 3 concise and relevant technical interview questions about {tech}. 

Do NOT include any introduction, explanation, or numbering except "1.", "2.", "3." before each question. 
Questions should be clear, unambiguous, and suitable for assessing candidate proficiency.

Example format:

1. First question here?
2. Second question here?
3. Third question here?

Only provide the 3 questions exactly as shown in the example above.
"""
