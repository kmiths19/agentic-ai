
from pymongo.collection import Collection


def ensure_text_index(collection: Collection) -> None:
    """Create a text index on the knowledge document fields."""
    collection.create_index(
        [
            ("title", "text"),
            ("content", "text"),
            ("tags", "text"),
        ],
        name="knowledge_text_index",
    )


def retrieve_documents(
    collection: Collection,
    question: str,
    limit: int = 3,
) -> list[dict]:
    """Retrieve documents matching the question's keywords."""
    if not question or not question.strip():
        raise ValueError("Question must not be empty.")

    if limit < 1:
        raise ValueError("Limit must be at least 1.")

    ensure_text_index(collection)

    cursor = collection.find(
        {"$text": {"$search": question.strip()}},
        {
            "_id": 0,
            "title": 1,
            "content": 1,
            "category": 1,
            "tags": 1,
            "score": {"$meta": "textScore"},
        },
    ).sort(
        [("score", {"$meta": "textScore"})]
    ).limit(limit)

    return list(cursor)
