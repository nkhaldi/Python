#!/usr/bin/env python3

# В этой задаче вам необходимо научиться генерировать html-код на питоне
# и сдать на проверку html-файл, в котором будет таблица размером 10 на 10,
# которая должна содержать таблицу умножения для чисел от 1 до 10.


fname = 'tests/mul_table.html'
with open(fname, 'w') as fd:
    fd.write('<html><body><table>')
    for i in range(1, 11):
        fd.write('<tr>')
        for j in range(1, 11):
            fd.write(f'<td> {i * j} </td>')
        fd.write('</tr>')
    fd.write('</table></body></html>')
