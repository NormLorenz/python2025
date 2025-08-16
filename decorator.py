import time
from typing import Any, Callable
from functools import wraps


def get_time(func: Callable) -> Callable:
    """Decorator to measure the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        start_time: float = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
    return wrapper


def repeat(n: int) -> Callable:
    """Decorator to repeat a function n times."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(n):
                print(f"Execution {i + 1}:")
                func(*args, **kwargs)
        return wrapper
    return decorator


@get_time
def calculate() -> None:
    """Function to perform a calculation."""
    print("Starting calculation...")
    time.sleep(3)  # Simulating a long calculation
    print("Calculation completed.")


@repeat(3)
def greet(name: str) -> None:
    """Function to greet a user."""
    print(f"Hello, {name}!")


def main() -> None:
    calculate()
    greet("Alice")


if __name__ == "__main__":
    main()
