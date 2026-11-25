from importlib import import_module
from typing import Any

from app.config import get_openai_config


def create_llm() -> Any:
    """Create an OpenAI chat model using application configuration."""
    config = get_openai_config()
    # Load dynamically so static analyzers do not require the optional package
    # to be installed in every environment where this module is inspected.
    chat_openai = import_module("langchain_openai").ChatOpenAI
    
    return chat_openai(
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
    response = llm.invoke(
        [
            ("system", "Your name is Golku"),
            ("human", question.strip()),
        ]
    )
    return str(response.content)
