# coding: utf-8
"""
Приложение, выводящее на экран спиральную матрицу.
"""
from centroid import Centroid
from matrix import Matrix


def gener_spriral_sqr_matrix(matrix):
    """
    Генератор линейного списка сформированного спирально из квадратной матрицы.

    :param matrix: двумерный список, длина каждого члена которого == длине списка.
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


def spiral_matrix(matrix):
    """
    Получение линейной спиральной матрицы из квадратной.

    :param matrix: двумерный список.
    :return:
    """
    return tuple(gener_spriral_sqr_matrix(matrix))


def main():
    matrix = Matrix.make_matrix()
    print("Your matrix:")
    print(matrix)

    print("-"*matrix.size)
    print("Answer:")

    mtrx = spiral_matrix(matrix)
    print(" ".join(str(x) for x in mtrx))


if __name__ == "__main__":
    main()
