"""Basic translation implementation using OpenAI."""
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate(text):
    """Translate text between Korean and English."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Fixed model for all translations
        messages=[
            {"role": "system", "content": """You are a highly skilled translator with expertise in many languages. Your task is to:
                - Identify if the input is Korean or English
                - If Korean, translate to English
                - If English, translate to Korean
                - Preserve meaning, tone, and nuance
                - Maintain proper grammar and formality level
                """},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        text = input("\nEnter text to translate (or 'q' to quit): ")
        if text.lower() == 'q':
            break
            
        result = translate(text)
        print(f"\nTranslation: {result}")
