"""Any module."""


def fact(n: int) -> int:
    """Get the factorial of n."""
    return n if n < 2 else n * fact(n - 1)


if __name__ == "__main__":
    print("Lib module is executed.")
    n = int(input("Enter n: "))
    print(f"Factorial of {n} is {fact(n)}.")
else:
    print("Lib module is imported.")
    print(type(__name__), __name__)
