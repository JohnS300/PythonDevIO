"""
greeting_app.main
"""


def greet(name: str) -> str:
    """Return a friendly greeting

    Args:
        name (str): User's name

    Returns:
        str: Greeting message
    """

    return f"Hello {name}! Welcome to Python Mastery"


def main() -> None:
    user_input = input("What's your name? ")
    print(greet(user_input))


if __name__ == "__main__":
    main()
