""" Пример использования библиотеки. """
from area import AreaCalcable, Circle, Triangle


if __name__ == '__main__':
    figs: list[AreaCalcable] = [Circle(5), Circle(12), Triangle(5, 3, 3), Triangle(11, 8, 6)]

    for fig in figs:
        print(fig.area())

    print(Triangle(5, 3, 3).is_right_triangle())
    print(Triangle(11, 8, 6).is_right_triangle())
