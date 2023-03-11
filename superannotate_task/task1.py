#!/usr/bin/env python3


def get_numbers_from_line(line):
    current, minus = None, 1
    numbers = list()
    digits_set = '0123456789'

    for char in line:
        if char == '-':
            if current is not None:
                numbers.append(current * minus)
            current, minus = None, -1
        elif char in digits_set:
            if current is None:
                current = int(char)
            else:
                current = current * 10 + int(char)
        elif current is not None:
            numbers.append(current * minus)
            current, minus = None, 1

    if current is not None:
        numbers.append(current * minus)

    return numbers


def get_numbers_sum(line):
    numbers = get_numbers_from_line(line)
    return sum(numbers)


def get_sums(numbers):
    pos_sum, neg_sum = 0, 0
    for number in numbers:
        if number > 0:
            pos_sum += number
        else:
            neg_sum += number

    return pos_sum, neg_sum


if __name__ == '__main__':
    input_line = input("Enter line to parse: ")
    # input_line = '-100#^sdfkj8902w3ir021@swf-20'
    numbers = get_numbers_from_line(input_line)
    total_sum = get_numbers_sum(input_line)
    pos_sum, neg_sum = get_sums(numbers)

    print("List of found numbers:", numbers)
    print("Sum of all numbers:", total_sum)
    print("Sum of positive numbers:", pos_sum)
    print("Sum of negative numbers:", neg_sum)
