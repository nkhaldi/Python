# Выведите таблицу размером nxn,
# заполненную числами от 1 до n^2 по спирали,
# выходящей из левого верхнего угла и
# закрученной по часовой стрелке, как показано в примере


def spiral(n):
    dx, dy = 1, 0
    x, y = 0, 0
    myarray = [[None] * n for j in range(n)]
    for i in range(1, n * n + 1):
        myarray[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == 0:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return myarray


def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print(myarray[x][y], end=' ')
        print()


n = int(input())
printspiral(spiral(n))
