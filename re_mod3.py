#!/usr/bin/env python3

"""
Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.
Решить задачу, используя регулярные выражения.
"""

import re
import sys


pattern = "^(0|(1(01*0)*1))*$"
pattern = re.compile(pattern)

for line in sys.stdin:
    line = line.rstrip()
    if pattern.match(line):
        print(line)
