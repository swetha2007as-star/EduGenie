import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")


def generate_quiz(topic):
    prompt = f"""
    Create 5 multiple-choice quiz questions about: {topic}

    For each question provide:
    1. Question
    2. Four options (A, B, C, D)
    3. Correct answer

    Keep the questions simple and educational.
    """

    response = model.generate_content(prompt)
    return response.text