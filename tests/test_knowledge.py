
from unittest.mock import MagicMock

from app.knowledge import (
    SAMPLE_DOCUMENTS,
    get_all_knowledge_documents,
    save_knowledge_documents,
)


def test_save_knowledge_documents():
    collection = MagicMock()

    count = save_knowledge_documents(
        collection,
        SAMPLE_DOCUMENTS,
    )

    assert count == 3
    assert collection.update_one.call_count == 3

    first_document = SAMPLE_DOCUMENTS[0]

    collection.update_one.assert_any_call(
        {"title": first_document["title"]},
        {"$set": first_document},
        upsert=True,
    )


def test_get_all_knowledge_documents():
    expected_documents = [
        {
            "title": "Database Configuration",
            "content": "Sample database information",
            "category": "database",
            "tags": ["mongodb"],
        }
    ]

    collection = MagicMock()
    cursor = MagicMock()
    cursor.sort.return_value = expected_documents
    collection.find.return_value = cursor

    result = get_all_knowledge_documents(collection)

    assert result == expected_documents
    collection.find.assert_called_once_with({}, {"_id": 0})
    cursor.sort.assert_called_once_with("title", 1)
