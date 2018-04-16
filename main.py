# coding: utf-8
"""
Приложение, выводящее на экран спиральную матрицу.
"""
from centroid import Centroid
from matrix import Matrix


def get_spriral_sqr_matrix(matrix):
    """
    Получение линейного списка сформированного спирально из квадратной матрице
    :param matrix:
    :return:
    """

    def get_vector_from_matrix(x, y):
        return matrix[x][y]

    col_size = len(matrix)
    if not all(len(row) == col_size for row in matrix):
        raise TypeError("Must be square")
    elif col_size < 3:
        raise TypeError("Min size = 3x3")

    median = int(col_size / 2)
    centroid = Centroid(median, median, col_size, col_size)
    yield get_vector_from_matrix(*centroid.vector)

    start_centroid = centroid

    for level in range(1, median+1):

        # left one step always
        start_centroid.left()
        yield get_vector_from_matrix(*centroid.vector)

        # down
        down_steps = 1+2*(level-1)
        for _ in range(down_steps):
            start_centroid.down()
            yield get_vector_from_matrix(*centroid.vector)

        # right
        right_steps = 2*level
        for _ in range(right_steps):
            start_centroid.right()
            yield get_vector_from_matrix(*centroid.vector)

        # up
        up_steps = 2*level
        for _ in range(up_steps):
            start_centroid.up()
            yield get_vector_from_matrix(*centroid.vector)

        # left
        left_steps = 2*level
        for _ in range(left_steps):
            start_centroid.left()
            yield get_vector_from_matrix(*centroid.vector)


def test_3_3():
    matrix = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ]

    spiral = " ".join((str(x) for x in get_spriral_sqr_matrix(matrix)))
    assert spiral == "5 4 7 8 9 6 3 2 1"


def test_5_5():
    matrix = [
        (1,  2,  3,  4,  5),
        (6,  7,  8,  9,  10),
        (11, 12, 13, 14, 15),
        (16, 17, 18, 19, 20),
        (21, 22, 23, 24, 25)
    ]

    etalon = "13 12 17 18 19 14 9 8 7 6 11 16 21 22 23 24 25 20 15 10 5 4 3 2 1"
    spiral = " ".join((str(x) for x in get_spriral_sqr_matrix(matrix)))
    assert etalon == spiral


if __name__ == "__main__":
    matrix = Matrix.make_matrix()
    print("=" * matrix.size)
    print("Your matrix:")
    print(matrix)

    print("Answer:")
    print(" ".join((str(x) for x in get_spriral_sqr_matrix(matrix))))
