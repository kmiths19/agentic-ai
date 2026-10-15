
from app import rag


def test_format_documents():
    documents = [
        {
            "title": "Database Configuration",
            "content": "The application uses MongoDB Atlas.",
            "category": "database",
        }
    ]

    result = rag.format_documents(documents)

    assert "Database Configuration" in result
    assert "The application uses MongoDB Atlas." in result
    assert "database" in result


def test_format_documents_when_empty():
    assert (
        rag.format_documents([])
        == "No relevant documents were found."
    )


def test_answer_question_when_no_documents(monkeypatch):
    monkeypatch.setattr(
        rag,
        "retrieve_documents",
        lambda collection, question: [],
    )

    result = rag.answer_question(
        collection=None, # pyright: ignore[reportArgumentType]
        question="What is the project about?",
    )

    assert "don't have enough information" in result["answer"]
    assert result["sources"] == []
