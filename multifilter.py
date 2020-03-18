# Одним из самых часто используемых классов в Python является класс filter.
# Он принимает в конструкторе два аргумента a и f – последовательность
# и функцию, и позволяет проитерироваться только по таким элементам x
# из последовательности a, что f(x) равно True. Будем говорить,
# что в этом случае функция f допускает элемент x,
# а элемент x является допущенным.

# В данной задаче мы просим вас реализовать класс multifilter,
# который будет выполнять ту же функцию, что и стандартный класс filter,
# но будет использовать не одну функцию, а несколько.

# Решение о допуске элемента будет приниматься на основании того,
# сколько функций допускают этот элемент, и сколько не допускают.
# Обозначим эти количества за pos и neg.

# Введем понятие решающей функции – это функция,
# которая принимает два аргумента – количества pos и neg,
# и возвращает True, если элемент допущен, и False иначе.

# Класс должен обладать следующей структурой:
"""
class multifilter:
    допускает элемент, если его допускает хотя бы половина фукнций pos >= neg)
    def judge_half(pos, neg):

    допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
    def judge_any(pos, neg):

    допускает элемент, если его допускают все функции (neg == 0)
    def judge_all(pos, neg):

    def __init__(self, iterable, *funcs, judge=judge_any):
    iterable - исходная последовательность
    funcs - допускающие функции
    judge - решающая функция

    возвращает итератор по результирующей последовательности
    def __iter__(self):
"""


a = [i for i in range(31)]


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


class multifilter:

    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for element in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(element):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield element
