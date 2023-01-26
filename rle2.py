#!/usr/bin/env python3

"""
Дана строка, содержащая буквы //A-Z//:
"AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
Нужно написать функцию RLE, которая выведет строку вида:
"A4B3C2XYZD4E3F3A6B28"
Еще надо выдавать ошибку, если на ввод приходит недопустимая строка.

Примечания:
1. Если символ встречается один раз, он остается неизменным
2. Если символ встречается более одного раза, к нему добавляется число повторений
"""

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def RLE(input_line):
    answer = list()
    current = ''
    counter = 0
    for el in input_line:
        if el not in letters:
            raise ValueError

        if current == '':
            current = el
            counter = 1
        elif el != current:
            answer.append(current)
            if counter > 1:
                answer.append(str(counter))
            current = el
            counter = 1
        else:
            counter += 1

    answer.append(current)
    if counter > 1:
        answer.append(str(counter))

    return ''.join(answer)
