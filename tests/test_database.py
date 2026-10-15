
from unittest.mock import MagicMock, patch

from app.database import (
    create_mongodb_client,
    get_documents_collection,
)


def test_create_mongodb_client():
    with patch(
        "app.database.MongoClient"
    ) as mock_client, patch(
        "app.database.get_mongodb_config",
        return_value={"uri": "mongodb://example"},
    ):
        create_mongodb_client()

        mock_client.assert_called_once_with(
            "mongodb://example",
            serverSelectionTimeoutMS=5000,
        )


def test_get_documents_collection():
    collection = MagicMock()
    database = MagicMock()
    database.__getitem__.return_value = collection
    client = MagicMock()
    client.__getitem__.return_value = database

    with patch(
        "app.database.get_mongodb_config",
        return_value={
            "uri": "mongodb://example",
            "database": "test_db",
            "collection": "test_docs",
        },
    ):
        result = get_documents_collection(client)

    assert result is collection
    client.__getitem__.assert_called_once_with("test_db")
    database.__getitem__.assert_called_once_with("test_docs")
