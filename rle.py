# Напишите функции, которые кодируют и декодируют
# сторку алгоритмом сжатия, где группы одинаковых
# символов исходной строки заменяются на этот символ
# и количество его повторений в этой позиции строки.

# Пример:
# encode_rle('aaaabbсdd') -> '4a2bс2d'
# decode_rle('4a2bс2d') -> 'aaaabbcdd'

import re

def encode_rle(inp):
    x = 1
    cnt = 1
    lst = list()
    curr = inp[x:x+1]

    for ch in inp:
        if ch in curr:
            cnt += 1
        else:
            if cnt == 1:
                lst += [str(ch)]
            else:
                lst += [str(cnt) + str(ch)]
            cnt = 1
        x += 1
        curr = inp[x:x+1]
    return ''.join(lst)

def decode_rle(inp):
    out = ""
    find_all = re.findall(r"(\d*)([a-zA-Z]{1})", inp)
    for k in find_all:
        if k[0] == '':
            out += k[1]
        else:
            out += k[1] * int(k[0])
    return out
