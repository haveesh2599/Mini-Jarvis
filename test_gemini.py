from dotenv import load_dotenv
from google import genai
import os

# Load the API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key was not found.")
    exit()

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Ask Gemini a question
response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="Explain artificial intelligence in simple words."
)

print("\nGemini says:")
print(response.text)