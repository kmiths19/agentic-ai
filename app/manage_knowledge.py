
from app.database import (
    create_mongodb_client,
    get_documents_collection,
)
from app.knowledge import (
    SAMPLE_DOCUMENTS,
    get_all_knowledge_documents,
    save_knowledge_documents,
)


def main() -> None:
    client = create_mongodb_client()

    try:
        client.admin.command("ping")
        collection = get_documents_collection(client)

        count = save_knowledge_documents(
            collection,
            SAMPLE_DOCUMENTS,
        )
        print(f"Processed {count} knowledge documents.\n")

        documents = get_all_knowledge_documents(collection)

        print("Knowledge base contents:")
        for document in documents:
            print(f"\nTitle: {document['title']}")
            print(f"Category: {document['category']}")
            print(f"Content: {document['content']}")
            print(f"Tags: {', '.join(document['tags'])}")

        print(f"\nTotal documents stored: {len(documents)}")
        
    except Exception as error:
        print("An error occurred while managing the knowledge base.")
        print(f"Error type: {type(error).__name__}")
        print(f"Error details: {error}")

    finally:
        client.close()


if __name__ == "__main__":
    main()
