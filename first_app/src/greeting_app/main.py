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
    clean_name = name.strip()
    if not clean_name:
        # “if not” is used to test the opposite of a condition.
        # The code inside the block will be executed if the condition is False
        raise ValueError
    clean_name = clean_name.title()  # Capitalize first letter of each word
    return f"Hello {clean_name}! Welcome to Python Mastery"


def main() -> None:
    user_input = input("What's your name? ")
    print(greet(user_input))


if __name__ == "__main__":
    main()
