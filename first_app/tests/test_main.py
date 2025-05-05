from greeting_app.main import greet  # type: ignore
import pytest


def test_greet_happy_path():
    assert greet("Tony") == "Hello Tony! Welcome to Python Mastery"


def test_greet_empty_raises():
    with pytest.raises(ValueError):
        greet("   ")
