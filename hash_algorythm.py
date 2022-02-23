#!/usr/bin/env python3

password = input()

hashed = hash(0)
for el in password:
    hashed += hash(el)
print(hashed)
