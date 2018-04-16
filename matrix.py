# coding: utf-8
"""
Интерфейс матрицы.
"""


class Matrix(list):

    """
    Класс, предоставляеющий интерфейс создания и отображения квадратной матрицы.
    """

    # разделитель элементов матрицы в stdin
    __SEP = " "

    @classmethod
    def __get_row(cls):
        """
        Создание вектора-строки из STDIN.
        В качестве разделителя используется сепаратор cls.__SEP.
        :return:
        """
        inp_row = input().strip().split(cls.__SEP)
        return tuple(map(int, inp_row))

    @classmethod
    def make_matrix(cls):
        """
        Создает двумерный список из введенных значений
        :return: square_matrix, size_of_matrix
        """
        matrix = []
        first_row = cls.__get_row()
        row_size = len(first_row)

        matrix.append(first_row)
        for _ in range(row_size - 1):
            row = cls.__get_row()
            if len(row) != row_size:
                raise TypeError("Matrix must be square")
            matrix.append(row)

        return cls(matrix)

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.__size = len(self)

    @property
    def size(self):
        return self.__size

    def __repr__(self):

        def foo(matrix):
            for row in matrix:
                yield " ".join(str(x) for x in row)

        return "\n".join(list(foo(self)))