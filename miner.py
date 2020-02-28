# Поле для игры сапёр представляет собой сетку размером nxm.
# В ячейке сетки может находиться или отсутствовать мина. 

# Напишите программу, которая выводит "решённое" поле,
# т.е. для каждой ячейки, не являющейся миной,
# указывается число мин, находящихся в соседних ячейках
# (учитывая диагональные направления)

# Формат ввода:
# На первой строке указываются два натуральных числа,
# после чего в n строках содержится описание поля
# в виде последовательности точек '.' и звёздочек '*',
# где точка означает пустую ячейку, а звёздочка − ячейку с миной.

# Формат вывода:
# n строк поля, в каждой ячейке которого будет либо число
# от 0 до 8, либо мина (обозначенная символом "*"),
# при этом число означает количество мин в соседних ячейках поля.

def count_mines(wfield, i , j):
    cnt = 0
    if wfield[i][j] == '*':
        return '*'
    else:
        if wfield[i - 1][j - 1] == '*':
            cnt += 1
        if wfield[i - 1][j] == '*':
            cnt += 1
        if wfield[i - 1][j + 1] == '*':
            cnt += 1
        if wfield[i][j - 1] == '*':
            cnt += 1
        if wfield[i][j + 1] == '*':
            cnt += 1
        if wfield[i + 1][j - 1] == '*':
            cnt += 1
        if wfield[i + 1][j] == '*':
            cnt += 1
        if wfield[i + 1][j + 1] == '*':
            cnt += 1
        return cnt

def solver(wfield, rows, cols):
    res = list()
    for i in range(rows):
        curr = list()
        for j in range(cols):
            cnt = count_mines(wfield, i + 1, j + 1)
            curr.append(str(cnt))
        res.append(curr)
    return res

ifield = list()
wfield = list()

rows, cols = [int(i) for i in input().split()]
for i in range(rows):
    ifield.append(input())

wfield.append('.' * (cols + 2))
for row in ifield:
    wfield.append('.' + row + '.')
wfield.append('.' * (cols + 2))

res = solver(wfield, rows, cols)
for i in range(rows):
    for j in range(cols):
        print(res[i][j], end = '')
    print()
