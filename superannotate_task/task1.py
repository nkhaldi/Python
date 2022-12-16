#!/usr/bin/env python3

input_line = input("Enter line to parse: ")
# input_line = '-100#^sdfkj8902w3ir021@swf-20'

current, minus = 0, 1
numbers = list()
digits_set = list('0123456789')

for char in input_line:
    if char == '-':
        minus = -1
    elif char in digits_set:
        current = current * 10 + int(char)
    elif current > 0:
        numbers.append(current * minus)
        current, minus = 0, 1

if current > 0:
    numbers.append(current * minus)

pos_sum, neg_sum, tot_sum = 0, 0, 0
for number in numbers:
    tot_sum += number
    if number > 0:
        pos_sum += number
    else:
        neg_sum += number

print("List of found numbers:", numbers)
print("Sum of all numbers:", tot_sum)
print("Sum of positive numbers:", pos_sum)
print("Sum of negative numbers:", neg_sum)
