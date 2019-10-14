# Напишите функции, которые кодируют и декодируют
# сторку алгоритмом сжатия, где группы одинаковых
# символов исходной строки заменяются на этот символ
# и количество его повторений в этой позиции строки.

# Пример:
# encode('aaaabbсdd') -> '4a2bс2d'
# decode('4a2bс2d') -> 'aaaabbcdd'

def encode(inp):
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
	res = ''.join(lst)
