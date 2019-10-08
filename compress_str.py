# Напишите функции, которые кодируют и декодируют
# сторку алгоритмом сжатия, где группы одинаковых
# символов исходной строки заменяются на этот символ
# и количество его повторений в этой позиции строки.

# Пример:
# 'aaaabbсaa' -> '4a2bс2a'

def encode(st):
	x = 1
	cnt = 1
	lst = list()
	curr = st[x:x+1]

	for ch in st:
		if ch in curr:
			cnt += 1
		else:
			if cnt == 1:
				lst += [str(ch)]
			else:
				lst += [str(cnt) + str(ch)]
			cnt = 1
		x += 1
		curr = st[x:x+1]
	res = ''.join(lst)
