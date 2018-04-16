# coding: utf-8
"""
Интерфейс центроида - вектора, осуществляющего перемещение по матрице.
"""


class Centroid(object):
    """
    Класс центроида.
    """
    __slots__ = ("__row_size", "__col_size", "__i", "__j")

    def __init__(self, i, j, row_size, col_size):
        self.__row_size = row_size
        self.__col_size = col_size
        self.__i = i
        self.__j = j

    def left(self):
        """
        Смещение центроида на шаг влево.
        """
        if self.__j == 0:
            raise Exception("left boarder")
        self.__j -= 1

    def down(self):
        """
        Смещение центроида на шаг вниз.
        """
        if self.__i == self.__col_size:
            raise Exception("down boarder")
        self.__i += 1

    def right(self):
        """
        Смещение центроида на шаг вправо.
        """
        if self.__j == self.__row_size:
            raise Exception("right boarder")
        self.__j += 1

    def up(self):
        """
        Смещение центроида на шаг вверх.
        """
        if self.__i == 0:
            raise Exception("upper boarder")
        self.__i -= 1

    @property
    def vector(self):
        """
        Текущее положение центроида на сетке.
        :return: tuple(int, int)
        """
        return self.__i, self.__j

    def __repr__(self):
        return str((self.__i, self.__j))