#!/usr/bin/env python3

input_line = input("Enter line to encrypt: ")
#input_line = 'the lazy dog jumped over the quick brown fox'


shift = 2
encrypted = str()
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

for char in input_line:
    if char in upper:
        encrypted += upper[(upper.index(char) + shift) % len(upper)]
    elif char in lower:
        encrypted += lower[(lower.index(char) + shift) % len(lower)]
    else:
        encrypted += char

print("Encrypted message:", encrypted)
