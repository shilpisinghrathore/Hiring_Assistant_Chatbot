# Hiring_Assistant_Chatbot

# TalentScout Hiring Assistant Chatbot

TalentScout is an AI-powered Streamlit web application designed to automate the technical screening process for job candidates. It uses OpenAI's GPT models to generate technical questions based on the candidate’s tech stack and interactively captures their responses.

## Features

- Collects candidate details (name, email, phone, experience, etc.)
- Accepts multiple tech stacks (e.g., Python, Java, Machine Learning)
- Dynamically generates 3 technical questions per tech stack using LLM
- Asks one question at a time and records the candidate’s responses
- Displays a summary of the responses at the end of the screening
- Validates email and phone input for accuracy
- Clean, professional UI built with Streamlit

---

## Project Structure

TalentScout_Hiring_Assistant/
│
├── app.py # Main Streamlit application
├── utils.py # OpenAI integration, email/phone validation
├── prompts.py # Prompt template for generating technical questions
└── README.md # Project documentation

## Tech Stack
Frontend: Streamlit
Backend: Python
LLM: OpenAI GPT-4 (via API)

## Environment Management: .env, python-dotenv

## Libraries Used
streamlit
openai
python-dotenv
re (built-in for validation)


Prompts are carefully engineered for two primary tasks:

Information Collection:
Simple, user-friendly forms to gather structured candidate data.
Technical Question Generation:
Based on the candidate’s specified tech stack, prompts like:

Generate 3 technical interview questions for a candidate with 2+ years of experience in Python.
Responses are parsed and displayed sequentially.

The design ensures prompt clarity, context preservation, and role-appropriate outputs.
