#!/usr/bin/env python3

"""
Визуализация гипотезы Коллатца (3n+1 дилеемма, сиракуузская пробле́ма)
Берём любое натуральное число n. Если оно чётное, то делим его на 2,
а если нечётное, то умножаем на 3 и прибавляем 1 (получаем 3n + 1).
Над полученным числом выполняем те же самые действия, и так далее.
Гипотеза Коллатца заключается в том,
что какое бы начальное число n мы ни взяли, рано или поздно мы получим единицу.
"""


from matplotlib import pyplot as plt


def get_counter(n: int):
    cnt = 0
    while (n > 1):
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        cnt += 1
    return cnt


def plot_result(X, Y):
    xmax = max(X)
    ymax = max(Y)
    plt.plot(X, Y)
    plt.grid(True)
    plt.title('3n+1 problem')
    plt.xlabel('Number n')
    plt.ylabel('Operations')
    plt.axis([0, xmax, 0, ymax+1])
    plt.show()


if __name__ == '__main__':
    nrange = int(input())

    X, Y = [], []
    max_n, max_cnt = 0, 0
    for n in range(1, nrange+1):
        X.append(n)
        cnt = get_counter(n)
        Y.append(cnt)

        if cnt > max_cnt:
            max_n = n
            max_cnt = cnt

    plot_result(X, Y)
    print(f"Max {max_n}: {max_cnt}")
