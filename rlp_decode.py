#!/usr/bin/env python3

"""
Человек привык работать с символьным отображением информации,
цифровые устройства хранят, обрабатывают и пересылают любую информацию
в виде чисел, а если быть более точным, в виде двоичных битов.
Разные структуры данных по разному выглядят для человека:
числа - последовательности цифр, строки - последовательности символов,
списки - последовательности символов со специальным форматированием.
Цифровому устройству нужно использовать специальные алгоритмы
для того, чтобы сохранить данные структуры в памяти или передать
по коммуникационному каналу. Процесс перевода структур данных в формат,
используемый для хранения и пересылки, называется сериализацией,
обратный процесс называется десериализацией.
Программное обеспечение Ethereum для сериализации и десериализации
данных использует метод RLP (Recursive Length Prefix,
https://github.com/ethereum/wiki/wiki/RLP).

Напишите программу, которая меняет порядок элементов на обратный
в сериализованной с использованием RLP кодирования структуре данных
по следующему правилу:
Если данные - число, то в нем меняется порядок с big-endian на little-endian.
Если данные - строка, то ее элементы представляются в обратном порядке.
Если данные - список, то его элементы представляются в обратном порядке.
"""

# Решение с подключенной библиотекой rlp
import rlp


with open('tests/rlp_input.txt', 'r') as in_fd:
    lines = map(lambda x: x.strip(), in_fd.readlines())

with open('tests/rlp_output1.txt', 'w') as out_fd:
    for hexStr in lines:
        decodedStr = rlp.decode(bytes.fromhex(hexStr))
        encodedHex = rlp.encode(decodedStr[::-1]).hex()
        print(encodedHex, file=out_fd)


# Решение без библиотки rlp
def rlpDecode(hexStr: str):
    if 0 <= int(hexStr[:2], 16) <= 191:
        return rlpDecodeString(hexStr)
    else:
        return rlpDecodeArray(hexStr)


def rlpDecodeString(hexStr: str):
    result = hexStr[:2]
    bsize = int(hexStr[:2], 16)
    if 128 <= bsize <= 183:
        for i in range(len(hexStr)-2, 1, -2):
            result += hexStr[i] + hexStr[i+1]
    elif 184 <= bsize <= 191:
        bsize -= 183
        for i in range(1, bsize + 1):
            result += hexStr[2*i:2*i+2]
        for i in range(len(hexStr)-2, 2*bsize+1, -2):
            result += hexStr[i] + hexStr[i+1]
    return result


def rlpDecodeArray(hexStr: str):
    elements = list()
    result = hexStr[:2]
    bsize = int(hexStr[:2], 16)
    if 192 <= bsize <= 247:
        i = 2
        while i < len(hexStr):
            el, isize = rlpDecodeArrayElement(hexStr[i:])
            elements.append(el)
            i += isize
    elif bsize <= 255:
        bsize -= 247
        for i in range(1, bsize+1):
            result += hexStr[2*i:2*i+2]
        i = 2*bsize + 2
        while i < len(hexStr):
            el, isize = rlpDecodeArrayElement(hexStr[i:])
            elements.append(el)
            i += isize
    result += ''.join(elements[::-1])
    return result


def rlpDecodeArrayElement(hexStr: str):
    size = 0
    bsize = int(hexStr[:2], 16)
    if 0 <= bsize <= 127:
        rsize = 2
    elif 128 <= bsize <= 183:
        bsize -= 128
        rsize = 2*bsize + 2
    elif 184 <= bsize <= 191:
        bsize -= 183
        size = bsize
        rsize = 4*size + 2
        result += hexStr[:rsize]
    elif 192 <= bsize <= 247:
        bsize -= 192
        rsize = 2*bsize + 2
    elif bsize <= 255:
        bsize -= 247
        rsize = 4*size + 2
    result = hexStr[:rsize]
    return (result, rsize)


# Main
with open('tests/rlp_input.txt', 'r') as in_fd:
    lines = map(lambda x: x.strip(), in_fd.readlines())

with open('tests/rlp_output2.txt', 'w') as out_fd:
    for line in lines:
        print(rlpDecode(line), file=out_fd)
