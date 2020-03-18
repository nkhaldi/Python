# Описать класс треугольник и реализовать для него следующие методы:
# + Периметр
# + Площадь
# + Визуализация

import matplotlib.pyplot as plt
import numpy as np


class Point():
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_
        print("Point", self.x, self.y)


class Triangle():
    def __init__(self, p1_, p2_, p3_):
        self.p1 = p1_
        self.p2 = p2_
        self.p3 = p3_
        self.l1 = self.tlen(p1_, p2_)
        self.l2 = self.tlen(p2_, p3_)
        self.l3 = self.tlen(p3_, p1_)
        print("I am created")

    def tlen(self, p1, p2):
        return np.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

    def perim(self):
        return self.l1 + self.l2 + self.l3

    def square(self):
        p = self.perim() / 2
        return np.sqrt(p * (p - self.l1) * (p - self.l2) * (p - self.l3))

    def vis(self):
        xarr = [self.p1.x, self.p2.x, self.p3.x, self.p1.x]
        yarr = [self.p1.y, self.p2.y, self.p3.y, self.p1.y]
        plt.title("Полученный треугольник")
        plt.plot(xarr, yarr)
        plt.show()


p1 = Point(1, 1)
p2 = Point(1, 4)
p3 = Point(5, 1)
tr = Triangle(p1, p2, p3)

print(tr.perim())
print(tr.square())
tr.vis()
