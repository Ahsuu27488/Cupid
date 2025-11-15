from os import environ
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()

# Get API Key
API_KEY = environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("Please provide GEMINI_API_KEY in .env file")

# Initialize external client with Gemini
external_client = AsyncOpenAI(
    base_url='https://generativelanguage.googleapis.com/v1beta/openai',
    api_key=API_KEY
)

# Model configuration
MODEL = "gemini-2.0-flash"

