from typing import Final

AUTHOR: Final[str] = "Norman F. Lorenz"
VERSION: Final[str] = "0.1.0"
COPYRIGHT: Final[str] = "2025 Norman F. Lorenz"

DESCRIPTION: Final = "A collection of Python scripts for greetings."


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to the Python world."


def farewell(name: str) -> str:
    """Return a farewell message."""
    return f"Goodbye, {name}! See you next time."


if __name__ == '__main__':
    print(greet("World"))  # Example usage of the greet function
    print(farewell("World"))  # Example usage of the farewell function
    print(DESCRIPTION)  # Print the description of the module
    print(AUTHOR)  # Print the author of the module
    print(VERSION)  # Print the version of the module
