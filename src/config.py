"""Minimal Gemini connection check."""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Set GOOGLE_API_KEY in .env before running this check."
        )

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Say hello in one sentence",
    )
    print(response.text)

if __name__ == "__main__":
    main()
