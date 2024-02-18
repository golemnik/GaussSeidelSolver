from tkinter import *
from calculations.matrix import *

# window = Tk()
# window.title("Tkinter")
# window.geometry("1200x800")
# window.mainloop()

matrix = Matrix(4, [
    [1, 2, -1, 2],
    [3, 25, 2, 2],
    [-2, 1, 4, 2],
    [-2, 1, 4, 1]
])
# matrix.print_matrix()
# print(matrix.check_diagonal())
print(determinant(matrix))
