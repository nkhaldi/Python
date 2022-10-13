#!/usr/bin/env python3

"""
Base58 кодирование используется в Bitcoin для получения
человекочитаемого адреса, который используется для получения крпитовалюты.
Для этого число, определяющее адрес, переводится в строку,
для кодирования которой используется алфавит состоящий из 58 символов,
включая строчные и заглавные буквы латинского алфавита и цифры,
исключая неоднозначные в некоторых шрифтах символы,
такие как 0 (ноль), O (заглавная o), I (заглавная i) и l (строчная L).
Напишите программу, которая бы определяла символ алфавита,
кроме символа '1', который используется в конкретном адресе Bitcoin
чаще других символов.
"""

import bitcoin as btc


fd = open('tests/btc_addr.txt')
lines = map(lambda line: line.rstrip(), fd.readlines())
fd.close()

symbols = dict()
for line in lines:
    hex_line = hex(int(line, 2))[2:]
    hex0_line = (40 - len(hex_line))*'0' + hex_line
    b58_line = btc.hex_to_b58check(hex0_line)
    for smb in b58_line:
        symbols[smb] = symbols[smb] + 1 if smb in symbols else 1

if '1' in symbols:
    del symbols['1']
print(max(symbols, key=lambda x: symbols[x]))
