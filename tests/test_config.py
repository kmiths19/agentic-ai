
import pytest

from app.config import (
    get_mongodb_config,
    get_openai_config,
    get_required_env,
)


def test_required_env_returns_value(monkeypatch):
    monkeypatch.setenv("TEST_SETTING", "hello")

    assert get_required_env("TEST_SETTING") == "hello"


def test_required_env_rejects_missing_value(monkeypatch):
    monkeypatch.delenv("TEST_SETTING", raising=False)

    with pytest.raises(
        ValueError,
        match="Environment variable .* is required but not set",
    ):
        get_required_env("TEST_SETTING")


def test_openai_config(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_MODEL", "test-model")

    config = get_openai_config()

    assert config == {
        "api_key": "test-key",
        "model": "test-model",
    }


def test_mongodb_config(monkeypatch):
    monkeypatch.setenv("MONGODB_URI", "mongodb://example")
    monkeypatch.setenv("MONGODB_DATABASE", "test_db")
    monkeypatch.setenv("MONGODB_COLLECTION", "test_docs")

    config = get_mongodb_config()

    assert config == {
        "uri": "mongodb://example",
        "database": "test_db",
        "collection": "test_docs",
    }
