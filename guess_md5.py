#!/usr/bin/env python3

from decimal import Decimal, getcontext
from hashlib import md5

# Set the precision high enough to handle the decimal places we expect
getcontext().prec = 5


def decode_md5(original_md5: str, digits: int):
    """Decode md5 hash and get the number."""
    num = Decimal("1.0")
    eps = Decimal(10 ** (-digits))
    max_value = Decimal("101.0")
    while num < max_value:
        # Format the number with one decimal place
        str_num = format(num, f".{digits}f")
        num_md5 = md5(str_num.encode()).hexdigest()
        if num_md5 == original_md5:
            return str_num
        num += eps


if __name__ == "__main__":
    original_md5 = input()
    print(f"MD5 hash of the entered number: {original_md5}")
    decoded_num = decode_md5(original_md5, 4)
    print("The answer is:", decoded_num)
