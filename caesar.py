# Напишите функцию, которая шифрует текст шифром Цезаря.
# caesar:
# Используемый алфавит − пробел и малые символы латинского
# алфавита: ' abcdefghijklmnopqrstuvwxyz'
# uni_caesar:
# Используются символы из интервала 1F600—1F64F
# таблицы символов Юникода. Используется кодировка UTF-8.

def caesar(s, n):
    res = ""
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    for e in s:
        res += alphabet[(alphabet.index(e) + n) % len(alphabet)]
    return res

def uni_caesar(s, n):
    res = ""
    init = "".join([chr(x) for x in range(128512, 128592)])
    for e in s:
        res += init[(init.index(e) + n) % len(init)]
    return res
