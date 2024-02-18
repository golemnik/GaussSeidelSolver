class Matrix:
    # matrix view loaded as rows
    # [
    # [1, 2, 3, 4],
    # [1, 2, 3, 4],
    # [1, 2, 3, 4],
    # [1, 2, 3, 4]
    # ]

    __rows: [[int]] = None
    __dimension: int = None

    def __init__(self, n: int, rows: [[int]]):
        self.__dimension = n
        self.__rows = rows

    def is_empty(self) -> bool:
        if self.__rows is None:
            return True
        return False

    def get_rows(self) -> [[int]]:
        return self.__rows

    def get_dimension(self):
        return self.__dimension

    def print_matrix(self):
        for row in self.__rows:
            i = 1
            for col in row:
                print(col, " ", sep="", end='')
                i += 1
            print("")

    def check_diagonal(self):
        i = 0
        j = 0
        while i < len(self.__rows):
            while j < len(self.__rows[i]):
                if i == j and self.__rows[i][j] == 0:
                    return False
                j += 1
            i += 1
            j = 0
        return True


def check_determinant(matrix: Matrix) -> bool:
    return determinant(matrix) != 0


def algebraic_addition(matrix: Matrix, ai: int, aj: int) -> int:
    rows: [[int]] = []
    row: [int] = []
    i = 0
    j = 0
    while i < len(matrix.get_rows()):
        while j < len(matrix.get_rows()[i]):
            if (i != ai) and (j != aj):
                row.append(matrix.get_rows()[i][j])
            j += 1
        if len(row) > 0:
            rows.append(row)
        row = []
        i += 1
        j = 0
    sub_matrix: Matrix = Matrix(len(rows), rows)
    return determinant(sub_matrix)


def determinant(matrix: Matrix) -> int:
    rows: [[int]] = matrix.get_rows()
    if matrix.get_dimension() == 1:
        return rows[0][0]
    if matrix.get_dimension() == 2:
        return rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]
    det = 0
    i = 0
    while i < len(rows):
        det += (-1)**i * matrix.get_rows()[0][i] * algebraic_addition(matrix, 0, i)
        i += 1
    return det





