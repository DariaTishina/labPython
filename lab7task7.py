"""
Написать класс Point, который в конструкторе принимает
координаты точки и содержит методы show(), move() и
dist(), где первый метод возвращает координаты точки, второй
принимает значения, на которые нужно сместить координаты
точки, и последний выводит расстояние по формуле
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Начальные координаты : " + str(self.x) + ";" + str(self.y))

    def move(self, x, y):
        self.x = x
        self.y = y
        print(self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dist(self, point):
        print(((self.x - point.get_x()) ** 2 + (self.y - point.get_y()) ** 2) ** 0.5)


pointobj = Point(1, 1)
new_point = Point(2, 2)


pointobj.dist(new_point)
