from calculations.matrix import Matrix


def gz(n: int, a: Matrix, b: Matrix, x: Matrix, eps: float, m: int):
    k = 1
    nu = 0
    while k < m:
        nu = 0
        for i in range(1, n):
            s = 0
            for j in range(1, i - 1):
                s = s + a.get_rows()[i][j] * x.get_rows()[0][j]
                s = round(s, 40)
            for j in range(i + 1, n):
                s = s + a.get_rows()[i][j] * x.get_rows()[0][j]
                s = round(s, 5)
            x_t = (b.get_rows()[i][0] - s) / a.get_rows()[i][i]
            x_t = round(x_t, 9)
            d = abs(x.get_rows()[0][i] - x_t)
            if d > nu:
                nu = d
            # if nu == 0:
            #     print("nu = 0, d = ", d)
            #     print("x", x.get_rows()[0][i], "x_t", x_t, "x - x_t", x.get_rows()[0][i] - x_t)
            #     x.print_matrix(" x =")
            x.get_rows()[0][i] = x_t
        if nu < eps:
            x.print_matrix("Solution found:")
            print("accuracy:", nu)
            print("iteration used:", k)
            return
        k += 1
    print("iteration limit reached.")
    print("reached accuracy:", nu, "instead of", eps)
    print("iteration used:", k)
    x.print_matrix("reached x values:")
    return
