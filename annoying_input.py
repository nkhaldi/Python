# Напишите функцию get_int(start_message, error_message, end_message),
# принимающую три строки в качестве аргументов. 
# Функция должна запрашивать у пользователя ввод до тех пор,
# пока не будет введено целое число (строка, принимаемая функцией int без ошибок). 

# Перед первым запросом ввода должен быть выведен аргумент start_message,
# после каждого ошибочного ввода нужно выводить значение строки
# error_message и при удачном вводе нужно вывести строку end_message
# и вернуть полученное целое число из функции (см. пример работы).
# Каждое выводимое сообщение должно находиться на отдельной строке.

def get_int(start_message, error_message, end_message):
	print(start_message)
	while True:
		try:
			inp = int(input())
			break
		except ValueError:
			print(error_message)
	print(end_message)
	return inp

inp = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
print("\ninp\t= " + str(inp))
print("type\t= " + str(type(inp)))
