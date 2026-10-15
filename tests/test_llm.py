
import pytest

from app import llm


def test_ask_llm_returns_response_text(monkeypatch):
    class FakeResponse:
        content = "Python is a programming language."

    class FakeLLM:
        def invoke(self, question):
            assert question == "What is Python?"
            return FakeResponse()

    monkeypatch.setattr(llm, "create_llm", lambda: FakeLLM())

    result = llm.ask_llm("What is Python?")

    assert result == "Python is a programming language."


def test_ask_llm_rejects_empty_question():
    with pytest.raises(ValueError, match="Question cannot be empty"):
        llm.ask_llm("   ")
