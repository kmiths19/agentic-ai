
from pymongo import MongoClient
from pymongo.collection import Collection

from app.config import get_mongodb_config


def create_mongodb_client() -> MongoClient:
    """Create a MongoDB client using application configuration."""
    config = get_mongodb_config()

    return MongoClient(
        config["uri"],
        serverSelectionTimeoutMS=5000,
    )


def get_documents_collection(
    client: MongoClient,
) -> Collection:
    """Return the configured knowledge documents collection."""
    config = get_mongodb_config()

    database = client[config["database"]]
    collection = database[config["collection"]]

    return collection
