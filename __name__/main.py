"""Test my_module import."""

from my_module import fact

if __name__ == "__main__":
    print("Main module is executed.")
    n = int(input("Enter n: "))
    print(f"Factorial of {n} is {fact(n)}.")
else:
    print("Main module is imported.")
    print(type(__name__), __name__)
