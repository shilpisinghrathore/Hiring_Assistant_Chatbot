
from dotenv import load_dotenv

load_dotenv()



import re
import os
from openai import OpenAI
from prompts import technical_questions_prompt

# Initialize OpenAI client with environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_llm_response(prompt: str, model: str = "gpt-4o-mini", temperature: float = 0.7) -> str:
    """
    Call OpenAI chat completion and return assistant reply as string.
    """
    try:
        messages = [
            {"role": "system", "content": "You are a helpful technical interview assistant."},
            {"role": "user", "content": prompt}
        ]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return "Sorry, I am having trouble generating questions at the moment."


def generate_questions_for_tech(tech: str) -> list[str]:
    """
    Generate exactly 3 technical questions for a given tech using the LLM.
    Returns a list of question strings.
    """
    prompt = technical_questions_prompt(tech)
    raw_response = get_llm_response(prompt)

    # Parse the numbered questions: lines starting with 1., 2., 3.
    questions = []
    for line in raw_response.splitlines():
        line = line.strip()
        match = re.match(r"^\d+\.\s*(.*)", line)
        if match:
            questions.append(match.group(1).strip())
    # Fallback: if parsing fails, return raw_response as single question
    if not questions:
        questions = [raw_response]

    return questions


def validate_email(email: str) -> bool:
    """
    Validates email format.
    """
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(email_regex, email) is not None


def validate_phone(phone: str) -> bool:
    """
    Validates phone number format.
    """
    phone_regex = r"^\+?[\d\s\-]{7,15}$"
    return re.match(phone_regex, phone) is not None
