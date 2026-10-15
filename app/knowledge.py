
from pymongo.collection import Collection

from app.database import (
    create_mongodb_client,
    get_documents_collection,
)


SAMPLE_DOCUMENTS = [
    {
        "title": "Project Architecture",
        "content": (
            "The AI Knowledge Assistant is a Python application. "
            "It uses LangChain to orchestrate language model calls, "
            "OpenAI to generate responses, and MongoDB Atlas to "
            "store knowledge documents."
        ),
        "category": "architecture",
        "tags": ["python", "langchain", "openai", "mongodb"],
    },
    {
        "title": "Database Configuration",
        "content": (
            "The application stores knowledge in the MongoDB Atlas "
            "database named ai_knowledge_assistant, using the "
            "documents collection. PyMongo is used to connect "
            "Python to MongoDB."
        ),
        "category": "database",
        "tags": ["mongodb", "pymongo", "database"],
    },
    {
        "title": "LangChain Integration",
        "content": (
            "LangChain provides the application workflow for "
            "communicating with an OpenAI chat model. The "
            "ChatOpenAI integration sends prompts and receives "
            "model-generated responses."
        ),
        "category": "integration",
        "tags": ["langchain", "openai", "llm"],
    },
]


def save_knowledge_documents(
    collection: Collection,
    documents: list[dict],
) -> int:
    """Insert or update documents using their titles as unique keys."""
    for document in documents:
        collection.update_one(
            {"title": document["title"]},
            {"$set": document},
            upsert=True,
        )

    return len(documents)


def get_all_knowledge_documents(
    collection: Collection,
) -> list[dict]:
    """Retrieve all knowledge documents, ordered by title."""
    return list(
        collection.find(
            {},
            {"_id": 0},
        ).sort("title", 1)
    )


def seed_knowledge_base() -> int:
    """Connect to Atlas and insert or update the sample documents."""
    client = create_mongodb_client()

    try:
        client.admin.command("ping")
        collection = get_documents_collection(client)

        return save_knowledge_documents(
            collection,
            SAMPLE_DOCUMENTS,
        )
    finally:
        client.close()
