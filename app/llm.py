from langchain_openai import ChatOpenAI
from app.config import get_openai_config


def create_llm() -> ChatOpenAI:
    """Create an OpenAI chat model using application configuration."""
    config = get_openai_config()
    
    return ChatOpenAI(
        model=config["model"],
        api_key=config["api_key"], # pyright: ignore[reportArgumentType]
        temperature=0,
        timeout=30,
        max_retries=2
    )
    
def ask_llm(question: str) -> str:
    """Send a question to the LLM and return its text response."""
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")
    
    llm = create_llm()
    response = llm.invoke(question.strip())
    return str(response.content)