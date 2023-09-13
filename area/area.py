""" Area lib. Библиотека вычисления площади геометрической фигуры."""
from typing import Protocol
from math import pi, sqrt
import unittest


class AreaCalcable(Protocol):
    """ Протокол геометрической фигуры с вычисляемой площадью. """
    def area(self) -> float:
        """ Вычислить площадь геометрической фигуры. """
        ...


class Circle:
    """ Окружность. """
    def __init__(self, radius: float):
        """

        :param radius: Радиус окружности
        """
        self.__radius = radius

    def area(self) -> float:
        return pi * self.__radius ** 2


class Triangle:
    """ Треугольник. """
    def __init__(self, size_a: float, size_b: float, size_c: float):
        """

        :param size_a: Сторона треугольника.
        :param size_b: Сторона треугольника.
        :param size_c: Сторона треугольника.
        """
        self.__a = size_a
        self.__b = size_b
        self.__c = size_c

    def is_right_triangle(self) -> bool:
        """ Треугольник прямоугольный? """
        site = [self.__a, self.__b, self.__c]
        site.sort()
        if site[2] ** 2 == site[0] ** 2 + site[1] ** 2:
            return True
        else:
            return False

    def area(self) -> float:
        p = (self.__a + self.__b + self.__c) / 2
        return sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))


class LibTest(unittest.TestCase):
    """ Класс тестов библиотеки. """

    @staticmethod
    def calc_s(figure: AreaCalcable):
        return figure.area()

    def test_circle(self):
        self.assertEqual(LibTest.calc_s(Circle(12)), pi * 12 ** 2)
        self.assertEqual(LibTest.calc_s(Circle(3)), pi * 3 ** 2)

    def test_triangle(self):
        self.assertEqual(LibTest.calc_s(Triangle(3, 4, 5)), 3 * 4 / 2)
        self.assertTrue(Triangle(3, 4, 5).is_right_triangle())
        self.assertFalse(Triangle(4, 4, 5).is_right_triangle())


if __name__ == '__main__':
    unittest.main()