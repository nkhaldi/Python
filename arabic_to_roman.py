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
# 4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа меньшего:
# IV, IX, XL, XC, CD и CM, соответственно.
#
# Формат ввода:
# Строка, содержащая натуральное число n, 0 < n < 40000.
# Формат вывода:
# Строка, содержащая число, закодированное в римской системе счисления.

def get_num(inp, pos):
	num = int(inp)
	dic = {
		0 : ('M', '?','?', '?'),
		1 : ('C', 'CD','D', 'CM'),
		2 : ('X', 'XL','L', 'XC'),
		3 : ('I', 'IV','V', 'IX')
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

def arabic_to_roman(inp):
	lst = list()

	for i in range(len(inp)):
		lst.append(get_num(inp[i], i))
	return ''.join(lst)

inp = input()
print(arabic_to_roman(inp))
