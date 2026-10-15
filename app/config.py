import os
from pathlib import Path

from dotenv import load_dotenv

#Locate the project root independently of the current terminal directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

#Load the .env file from the project root
load_dotenv(PROJECT_ROOT / ".env")

def get_required_env(name: str) -> str:
    """Return a required environment variable or raise a clear error."""
    value = os.getenv(name)
    
    if value is None or not value.strip():
        raise ValueError(f"Environment variable '{name}' is required but not set.")
    return value.strip()

def get_openai_config() -> dict[str, str]:
    """Return the configuration needed for the OpenAI integration."""
    return {
        "api_key": get_required_env("OPENAI_API_KEY"),
        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini"
    }
    
def get_mongodb_config() -> dict[str, str]:
    """Return the configuration needed for the MongoDB integration."""
    return {
        "uri": get_required_env("MONGODB_URI"),
        "database": os.getenv("MONGODB_DATABASE", "ai_knowledge_assistant").strip(),
        "collection": os.getenv("MONGODB_COLLECTION", "documents").strip()
    }