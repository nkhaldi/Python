# В римской системе счисления для обозначения чисел
# используются следующие символы:
#
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#
# Будем использовать вариант, в котором числа
# 4, 9, 40, 90, 400 и 900 записываются как вычитание
# из большего числа меньшего:
# IV, IX, XL, XC, CD и CM, соответственно.
#
# Написать функции для перевода чисел:
# - из римской системы в десятичную
# - из десятичной системы в римскую


def get_num(inp, pos):
    num = int(inp)
    dic = {
        0: ('M', '?', '?', '?'),
        1: ('C', 'CD', 'D', 'CM'),
        2: ('X', 'XL', 'L', 'XC'),
        3: ('I', 'IV', 'V', 'IX')
    }
    one, four, five, nine = dic[pos]
    if num < 4:
        return one * num
    elif num == 4:
        return four
    elif 4 < num < 9:
        return five + (one * (num - 5))
    elif num == 9:
        return nine


def decimal_to_roman(inp):
    lst = list()
    if int(inp) > 9999:
        return 'The number is too big'
    if int(inp) < 10:
        inp = '000' + inp
    elif int(inp) < 100:
        inp = '00' + inp
    elif int(inp) < 1000:
        inp = '0' + inp
    for i in range(len(inp)):
        lst.append(get_num(inp[i], i))
    return ''.join(lst)


def roman_to_decimal(inp):
    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    rom = 0
    while inp:
        if len(inp) == 1 or dic[inp[0]] >= dic[inp[1]]:
            rom += dic[inp[0]]
            inp = inp[1:]
        else:
            rom += dic[inp[1]] - dic[inp[0]]
            inp = inp[2:]
    return rom
