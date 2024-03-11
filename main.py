from calculations.calculate import *
from calculations.fr import *

name = input("Write file <name> (without extension) or \"hand\" or \"gen\" for generated matrix:")
if name != "gen" and name != "hand":
    read_file(name)
elif name == "hand":
    rows = []
    while True:
        n = input("Write matrix size:")
        try:
            n = int(n)
            break
        except ValueError:
            print("Rewrite n as integer. ", end="")

    while True:
        eps = input("Write accuracy:")
        try:
            eps = float(eps)
            break
        except ValueError:
            print("Rewrite n as float. ", end="")
    print("Write ", n, " matrix lines in the format:")
    print("1 2 3 4")
    print("Where first digits are odds and last one is equal digit. Incorrect input will cause program to stop.")
    for i in range(0, n):
        row = input("Write new line:\n")
        row = row.replace(",", ".")
        row = row.split(" ")
        row = [r.rstrip("\n") for r in row]
        try:
            row = [float(r) for r in row]
        except ValueError:
            print("incorrect data found. Process stopped")
            exit(1)
        rows.append(row)
    a_t, b_t = [], []
    for i in range(0, n):
        a_t.append(rows[i][0:-1])
        b_t.append([rows[i][n]])
    a, b, x = Matrix(), Matrix(), Matrix()
    a.create_m(n, a_t)
    b.create_m(n, b_t)
    x.create_v2_unit_dim(n)

    print("n:", n, "eps:", eps)
    a.print_matrix("a odds")
    b.print_matrix("b odds")
    x.print_matrix("x prediction")

    a.diagonal_predominance()
    if not a.check_diagonal():
        print("Attempt for diagonal predominance failed. Results may be unpredicted.")
        a.print_matrix("a odds final state:")
    gz(n, a, b, x, eps, 300)
else:
    while True:
        n = input("Write matrix size:")
        try:
            n = int(n)
            break
        except ValueError:
            print("Rewrite n as integer. ", end="")
    a, b, x = Matrix(), Matrix(), Matrix()
    a.create_m_rand_dim(n)
    b.create_v_rand_dim(n)
    x.create_v2_zero_dim(n)

    a.print_matrix("a odds")
    b.print_matrix("b odds")
    x.print_matrix("x prediction")

    a.diagonal_predominance()
    if not a.check_diagonal():
        print("Attempt for diagonal predominance failed. Results may be unpredicted.")

    gz(n, a, b, x, 0.001, 300)






