from calculations.calculate import gz
from calculations.matrix import Matrix


def read_file(file_name):
    try:
        rows = []
        with open(file_name + ".txt", "r") as file:
            for line in file:
                row = line.replace(",", ".")
                row = row.split(" ")
                row = [r.rstrip("\n") for r in row]
                try:
                    row = [float(r) for r in row]
                except ValueError:
                    print("incorrect data found. Process stoped")
                    return
                rows.append(row)
            # print(rows)

        n = len(rows) - 1
        eps = rows[0][0]
        a_t = []
        b_t = []
        for i in range(1, n+1):
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
    except:
        print("file not exists")
