import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")

def summarize_text(text):
    try:
        response = model.generate_content(f"Summarize the following article:\n\n{text}")
        return response.text.strip()
    except Exception as e:
        return f"Error summarizing: {e}"
