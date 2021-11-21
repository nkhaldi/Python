#!/usr/bin/env python3

# Человек привык работать с символьным отображением информации,
# цифровые устройства хранят, обрабатывают и пересылают любую информацию
# в виде чисел, а если быть более точным, в виде двоичных битов.
# Разные структуры данных по разному выглядят для человека:
# числа - последовательности цифр, строки - последовательности символов,
# списки - последовательности символов со специальным форматированием.
# Цифровому устройству нужно использовать специальные алгоритмы
# для того, чтобы сохранить данные структуры в памяти или передать
# по коммуникационному каналу. Процесс перевода структур данных в формат,
# используемый для хранения и пересылки, называется сериализацией,
# обратный процесс называется десериализацией.
# Программное обеспечение Ethereum для сериализации и десериализации
# данных использует метод RLP (Recursive Length Prefix,
# https://github.com/ethereum/wiki/wiki/RLP).
#
# Напишите программу, которая меняет порядок элементов на обратный
# в сериализованной с использованием RLP кодирования структуре данных
# по следующему правилу:
# Если данные - число, то в нем меняется порядок с big-endian на little-endian.
# Если данные - строка, то ее элементы представляются в обратном порядке.
# Если данные - список, то его элементы представляются в обратном порядке.


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
    bits = hexStr[:2]
    if 0 <= int(bits, 16) <= 191:
        return rlpDecodeString(hexStr)
    else:
        return rlpDecodeArray(hexStr)


def rlpDecodeString(hexStr: str):
    result = str()
    bits = hexStr[:2]
    result += bits
    if 128 <= int(bits, 16) <= 183:
        for i in range(len(hexStr)-2, 1, -2):
            result += hexStr[i] + hexStr[i+1]
    elif 184 <= int(bits, 16) <= 191:
        size = int(bits, 16) - 183
        for i in range(1, int(bits, 16) - 183 + 1):
            bits = hexStr[2*i:2*i+2]
            result += bits
        for i in range(len(hexStr) - 2, 1+size*2, -2):
            result += hexStr[i] + hexStr[i+1]
    return result


def rlpDecodeArray(hexStr: str):
    result = str()
    elements = list()
    bits = hexStr[:2]
    result += bits
    if 192 <= int(bits, 16) <= 247:
        i = 2
        while i < len(hexStr):
            bits = hexStr[i:i+2]
            if 0 <= int(bits, 16) <= 191:
                el, isize = rlpDecodeStringFromArray(hexStr[i:])
                elements.append(el)
                i += isize
            elif int(bits, 16) <= 255:
                el, isize = rlpDecodeArrayFromArray(hexStr[i:])
                elements.append(el)
                i += isize
    elif int(bits, 16) <= 255:
        bsize = int(bits, 16) - 247
        for i in range(1, int(bits, 16) - 247 + 1):
            bits = hexStr[2*i:2*i+2]
            result += bits
        i = bsize*2 + 2
        while i < len(hexStr):
            bits = hexStr[i:i+2]
            if 0 <= int(bits, 16) <= 191:
                el, isize = rlpDecodeStringFromArray(hexStr[i:])
                elements.append(el)
                i += isize
            elif int(bits, 16) <= 255:
                el, isize = rlpDecodeArrayFromArray(hexStr[i:])
                elements.append(el)
                i += isize
    result += ''.join(elements[::-1])
    return result


def rlpDecodeStringFromArray(hexStr: str):
    result = str()
    size = 0
    bits = hexStr[:2]
    if 0 <= int(bits, 16) <= 127:
        result += bits
        size = 2
    elif int(bits, 16) <= 183:
        size = int(bits, 16) - 128
        result += hexStr[:2+size*2]
        size = 2+size*2
    elif int(bits, 16) <= 191:
        bsize = int(bits, 16) - 183
        bits = hexStr[2:2*bsize+2]
        size = int(bits, 16)
        result += hexStr[:size*2+bsize*2+2]
        size = size*2+bsize*2+2
    return (result, size)


def rlpDecodeArrayFromArray(hexStr: str):
    result = str()
    size = 0
    bits = hexStr[:2]
    if 192 <= int(bits, 16) <= 247:
        size = int(bits, 16) - 192
        result += hexStr[:2+size*2]
        size = 2 + size*2
    elif int(bits, 16) <= 255:
        bsize = int(bits, 16) - 247
        bits = hexStr[2:2*bsize+2]
        size = int(bits, 16)
        result += hexStr[:size*2+bsize*2+2]
        size = size*2+bsize*2+2
    return (result, size)


# Main
with open('tests/rlp_input.txt', 'r') as in_fd:
    lines = map(lambda x: x.strip(), in_fd.readlines())

with open('tests/rlp_output2.txt', 'w') as out_fd:
    for line in lines:
        print(rlpDecode(line), file=out_fd)
