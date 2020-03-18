# Требуется написать программу, осуществляющую преобразование
# из одних единиц измерения длины в другие.
# Должны поддерживаться
#   мили (1 mile = 1609 m),
#   ярды (1 yard = 0.9144 m),
#   футы (1 foot = 30.48 cm),
#   дюймы (1 inch = 2.54 cm),
#   километры (1 km = 1000 m),
#   метры (m),
#   сантиметры (1 cm = 0.01 m)
#   миллиметры (1 mm = 0.001 m)
#
# Формат ввода:
# Одна строка с фразой следующего вида:
# <number> <unit_from> in <unit_to>
# Формат вывода:
# Дробное число в научном формате (экспоненциальном),
# с точностью ровно два знака после запятой.


def translate(num, unit_from, unit_to):
    dict_to_m = {
        'mile': 1609,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001
    }
    dict_from_m = {
        'mile': 1 / 1609,
        'yard': 1 / 0.9144,
        'foot': 1 / 0.3048,
        'inch': 1 / 0.0254,
        'km': 1 / 1000,
        'm': 1 / 1,
        'cm': 1 / 0.01,
        'mm': 1 / 0.001
    }
    return num * dict_to_m[unit_from] * dict_from_m[unit_to]


num, unit_from, unit_in, unit_to = input().split(' ')
res = translate(float(num), unit_from, unit_to)
print("{:.2e}".format(res))
