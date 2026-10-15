
from pymongo.errors import PyMongoError

from app.database import (
    create_mongodb_client,
    get_documents_collection,
)


def main() -> None:
    client = None

    try:
        client = create_mongodb_client()

        # Force a real request to MongoDB Atlas.
        client.admin.command("ping")

        collection = get_documents_collection(client)

        print("MongoDB Atlas connection successful!")
        print(f"Database: {collection.database.name}")
        print(f"Collection: {collection.name}")

    except PyMongoError as error:
        print("Could not connect to MongoDB Atlas.")
        print(f"Error type: {type(error).__name__}")

    finally:
        if client is not None:
            client.close()


if __name__ == "__main__":
    main()
