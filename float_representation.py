#!/usr/bin/env python3

"""
Скрипт для наглядной демонстрации представления числе с плаваующей точкой
в языке Python в памяти компьютера
"""

import struct
from itertools import islice


def float_to_bin_parts(number, bits=64):
    if bits == 32:  # single precision
        int_pack = "I"
        float_pack = "f"
        exponent_bits = 8
        mantissa_bits = 23
    elif bits == 64:  # double precision. all python floats are this
        int_pack = "Q"
        float_pack = "d"
        exponent_bits = 11
        mantissa_bits = 52
    else:
        raise ValueError("bits argument must be 32 or 64")

    value = bin(struct.unpack(int_pack, struct.pack(float_pack, number))[0])
    bin_iter = iter(bin(value)[2:].rjust(bits, "0"))
    return ["".join(islice(bin_iter, x)) for x in (1, exponent_bits, mantissa_bits)]


if __name__ == "__main__":
    initial_number = float(input("Укажите ваше число: "))
    print("Элементы числа %.51f типа float:" % initial_number)
    print(float_to_bin_parts(initial_number, 64))
    sign, exponent, mantissa = float_to_bin_parts(initial_number, 64)

    print("Исходный порядок в десятичном виде: " + str(int(exponent, 2)))
    print("Настоящий порядок в двоичном виде: " + str(bin(int(exponent, 2) - 1023)))
    print("Настоящая мантисса в двоичном виде: " + str("1." + mantissa))

    exponent = int(exponent, 2) - 1023 - 52
    print("Порядок после переноса запятой (в десятичной системе): " + str(exponent))
    mantissa = int("1" + mantissa, 2)
    print("Мантисса после переноса запятой (в десятичной системе): " + str(mantissa))

    recon_number = mantissa * (2.0**exponent)

    if sign == "1":
        recon_number *= -1

    print("Реконструированное число {0:.52}".format(recon_number))
