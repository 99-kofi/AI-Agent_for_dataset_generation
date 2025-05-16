import requests
import os
from dotenv import load_dotenv

load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def search_google(query, num_results=10):
    headers = {"X-API-KEY": SERPER_API_KEY}
    payload = {"q": query, "num": num_results}
    response = requests.post("https://google.serper.dev/search", json=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("organic", [])
