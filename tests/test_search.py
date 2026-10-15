
import pytest
from unittest.mock import MagicMock

from app.search import retrieve_documents


def test_retrieve_documents():
    expected = [
        {
            "title": "Database Configuration",
            "content": "The application uses MongoDB Atlas.",
            "category": "database",
            "tags": ["mongodb"],
            "score": 1.5,
        }
    ]

    collection = MagicMock()
    cursor = MagicMock()

    collection.find.return_value = cursor
    cursor.sort.return_value = cursor
    cursor.limit.return_value = expected

    result = retrieve_documents(collection, "MongoDB")

    collection.create_index.assert_called_once()
    collection.find.assert_called_once()
    cursor.limit.assert_called_once_with(3)
    assert result == expected


def test_retrieve_documents_rejects_empty_question():
    collection = MagicMock()

    with pytest.raises(ValueError, match="Question must not be empty"):
        retrieve_documents(collection, "   ")

    collection.find.assert_not_called()
    collection.create_index.assert_not_called()


def test_retrieve_documents_rejects_invalid_limit():
    collection = MagicMock()

    with pytest.raises(ValueError, match="Limit must be at least 1"):
        retrieve_documents(collection, "MongoDB", limit=0)

    collection.find.assert_not_called()
