#!/usr/bin/env python3

"""
Хэширование паролей
"""

password = input()

hashed = hash(0)
for el in password:
    hashed += hash(el)
print(hashed)
