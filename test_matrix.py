
class Coord(object):

    def __init__(self, i, j, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.i = i
        self.j = j

    def left(self):
        if self.j == 0:
            raise Exception("left boarder")
        self.j -= 1

    def down(self):
        if self.i == self.col_size:
            raise Exception("down boarder")
        self.i += 1

    def right(self):
        if self.j == self.row_size:
            raise Exception("right boarder")
        self.j += 1

    def up(self):
        if self.i == 0:
            raise Exception("upper boarder")
        self.i -= 1

    def curent(self):
        return (self.i, self.j)

    def __repr__(self):
        return str((self.i, self.j))


def get_spriral_sqr_matrix(matrix):
    col_size = len(matrix)
    if not all(len(row) == col_size for row in matrix):
        raise TypeError("Must be square")
    elif col_size < 3:
        raise TypeError("Min size = 3x3")

    median = int(col_size / 2)
    centroid = Coord(median, median, col_size, col_size)
    yield matrix[centroid.i][centroid.j]

    start_centroid = centroid

    for level in range(1, median+1):

        # left one step always
        start_centroid.left()
        yield matrix[start_centroid.i][start_centroid.j]

        # down
        down_steps = 1+2*(level-1)
        for _ in range(down_steps):
            start_centroid.down()
            yield matrix[start_centroid.i][start_centroid.j]

        # right
        right_steps = 2*level
        for _ in range(right_steps):
            start_centroid.right()
            yield matrix[start_centroid.i][start_centroid.j]

        # up
        up_steps = 2*level
        for _ in range(up_steps):
            start_centroid.up()
            yield matrix[start_centroid.i][start_centroid.j]

        # left
        left_steps = 2*level
        for _ in range(left_steps):
            start_centroid.left()
            yield matrix[start_centroid.i][start_centroid.j]


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


def get_row():
    return tuple(map(int, input().strip()))


if __name__ == "__main__":
    matrix = []
    first_row = get_row()
    matrix_size = len(first_row)

    matrix.append(first_row)
    for _ in range(matrix_size-1):
        matrix.append(get_row())

    print(" ".join((str(x) for x in get_spriral_sqr_matrix(matrix))))
