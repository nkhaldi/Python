#!/usr/bin/env python3


def get_numbers_from_line(line):
    current, minus = 0, 1
    numbers = list()
    digits_set = '0123456789'

    for char in line:
        if char == '-':
            minus = -1
        elif char in digits_set:
            current = current * 10 + int(char)
        elif current > 0:
            numbers.append(current * minus)
            current, minus = 0, 1

    if current > 0:
        numbers.append(current * minus)

    return numbers


def get_sums(numbers):
    tot_sum, pos_sum, neg_sum = 0, 0, 0
    for number in numbers:
        tot_sum += number
        if number > 0:
            pos_sum += number
        else:
            neg_sum += number

    return tot_sum, pos_sum, neg_sum


input_line = input("Enter line to parse: ")
# input_line = '-100#^sdfkj8902w3ir021@swf-20'
numbers = get_numbers_from_line(input_line)
tot_sum, pos_sum, neg_sum = get_sums(numbers)

print("List of found numbers:", numbers)
print("Sum of all numbers:", tot_sum)
print("Sum of positive numbers:", pos_sum)
print("Sum of negative numbers:", neg_sum)
