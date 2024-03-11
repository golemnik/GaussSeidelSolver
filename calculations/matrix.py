import copy
import random


class Matrix:
    # matrix view loaded as rows
    # [
    # [1, 2, 3, 4],
    # [1, 2, 3, 4],
    # [1, 2, 3, 4],
    # [1, 2, 3, 4]
    # ]

    __rows: [[float]] = None
    __dimension: int = None

    def __init__(self):
        return

    def create_m(self, n: int, rows: [[float]]):
        self.__dimension = n
        self.__rows = rows

    def create_m_rand(self):
        self.__dimension = random.randint(1, 9)
        rows = []
        i, j = 0, 0
        while i < self.__dimension:
            rows.append([])
            while j < self.__dimension:
                rows[i].append(round(random.uniform(-2.9, 2.9), 2))
                j += 1
            j = 0
            i += 1
        self.__rows = rows

    def create_m_rand_dim(self, max_n):
        self.__dimension = max_n
        rows = []
        i, j = 0, 0
        while i < self.__dimension:
            rows.append([])
            while j < self.__dimension:
                rows[i].append(round(random.uniform(-9.9, 9.9), 5))
                j += 1
            j = 0
            i += 1
        self.__rows = rows

    def create_v_rand_dim(self, max_n):
        self.__dimension = max_n
        rows = []
        i, j = 0, 0
        rows.append([])
        while i < self.__dimension:
            rows.append([])
            rows[i].append(round(random.uniform(-9.9, 9.9), 5))
            i += 1
        self.__rows = rows

    def create_v2_rand_dim(self, max_n):
        self.__dimension = max_n
        rows = []
        i, j = 0, 0
        rows.append([])
        while j < self.__dimension:
            rows[i].append(round(random.uniform(-9.9, 9.9), 5))
            j += 1
        self.__rows = rows

    def create_v_unit_dim(self, max_n):
        self.__dimension = max_n
        rows = []
        i, j = 0, 0
        rows.append([])
        while i < self.__dimension:
            rows.append([])
            rows[i].append(1)
            i += 1
        self.__rows = rows

    def create_v2_unit_dim(self, max_n):
        self.__dimension = max_n
        rows = []
        i, j = 0, 0
        rows.append([])
        while j < self.__dimension:
            rows[i].append(1)
            j += 1
        self.__rows = rows

    def create_m_zero(self, n: int):
        self.__dimension = n
        rows = []
        i, j = 0, 0
        while i < n:
            rows.append([])
            while j < n:
                rows[i].append(0)
                j += 1
            j = 0
            i += 1
        self.__rows = rows

    def create_v_zero_dim(self, max_n):
        self.__dimension = max_n
        rows = []
        i, j = 0, 0
        rows.append([])
        while i < self.__dimension:
            rows.append([])
            rows[i].append(0)
            i += 1
        self.__rows = rows

    def create_v2_zero_dim(self, max_n):
        self.__dimension = max_n
        rows = []
        i, j = 0, 0
        rows.append([])
        while j < self.__dimension:
            rows[i].append(0)
            j += 1
        self.__rows = rows

    def is_empty(self) -> bool:
        if self.__rows is None:
            return True
        return False

    def get_rows(self) -> [[int]]:
        return self.__rows

    def get_dimension(self):
        return self.__dimension

    def print_matrix(self, comment):
        # print("Dimension:", self.__dimension)
        # print("Matrix:")
        print(comment)
        # print(self.__rows)
        for i in range(0, len(self.__rows)):
            for j in range(0, len(self.__rows[i])):
                print(self.__rows[i][j], " ", sep="", end='')
            print("")
        print("")

    def max_index(self, row):
        m, index = 0, 0
        for i in range(0, len(row)):
            if abs(row[i]) > m:
                m = abs(row[i])
                index = i
        return index

    def check_diagonal(self):
        i, j = 0, 0
        while i < len(self.__rows):
            s = 0
            while j < len(self.__rows[i]):
                s += abs(self.__rows[i][j])
                j += 1
            if abs(self.__rows[i][i]) < s-abs(self.__rows[i][i]):
                return False
            j = 0
            i += 1
        return True

    def swap_rows(self, n1, n2):
        if (n1 > self.__dimension) or (n2 > self.__dimension):
            return
        rows = copy.deepcopy(self.__rows)
        rows[n1] = self.__rows[n2]
        rows[n2] = self.__rows[n1]
        self.__rows = rows

    def swap_colons(self, n1, n2):
        if (n1 > self.__dimension) or (n2 > self.__dimension):
            return
        rows = copy.deepcopy(self.__rows)
        i = 0
        while i < len(self.__rows):
            rows[i][n1] = self.__rows[i][n2]
            rows[i][n2] = self.__rows[i][n1]
            i += 1
        self.__rows = rows

    def diagonal_predominance(self):
        i, j = 0, 0
        while i < self.__dimension:
            while j < self.__dimension:
                self.swap_colons(i, self.max_index(self.__rows[i]))
                j += 1
            i += 1
            j = 0
        return


def add_matrix(matrix_a: Matrix, matrix_b: Matrix) -> bool:
    if (matrix_a is None) or (matrix_b is None):
        print("one matrix is None")
        return False
    if matrix_a.get_dimension() != matrix_b.get_dimension():
        print("wrong dimensions")
        return False
    for row in matrix_a.get_rows():
        for column in row:
            matrix_a.get_rows()[row][column] += matrix_b.get_rows()[row][column]
    return True


def check_determinant(matrix: Matrix) -> bool:
    return determinant(matrix) != 0


def algebraic_addition(matrix: Matrix, ai: int, aj: int) -> float:
    rows: [[float]] = []
    row: [float] = []
    i, j = 0, 0
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
    sub_matrix: Matrix = Matrix()
    sub_matrix.create_m(len(rows), rows)
    return determinant(sub_matrix)


def determinant(matrix: Matrix) -> float:
    rows: [[float]] = matrix.get_rows()
    if matrix.get_dimension() == 1:
        return rows[0][0]
    if matrix.get_dimension() == 2:
        return rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]
    det = 0
    i = 0
    while i < len(rows):
        det += (-1) ** i * matrix.get_rows()[0][i] * algebraic_addition(matrix, 0, i)
        i += 1
    return det
