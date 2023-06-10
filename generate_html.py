#!/usr/bin/env python3

"""
Вам нужно сгенерировать html-код на питоне и сдать на проверку
html-файл, в котором будет таблица размером 10 на 10,
которая должна содержать таблицу умножения для чисел от 1 до 10.
Каждое число в таблице должно быть ссылкой на страницу
http://<это число>.ru. Например, число 12 должно быть
ссылкой на страницу http://12.ru.
"""

fname = "tests/mul_table.html"
with open(fname, "w") as fd:
    fd.write("<html><body><table>")
    for i in range(1, 11):
        fd.write("<tr>")
        for j in range(1, 11):
            mul = i * j
            fd.write(f"<td><a href=http://{mul}.ru>{mul}</a></td>")
        fd.write("</tr>")
    fd.write("</table></body></html>")
