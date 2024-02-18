class Equation:
    def __init__(self, coefficients, result):
        self.__coefficients = coefficients
        self.__result = result

    def __div_equation__(self, n):
        i = 0
        while i < len(self.__coefficients):
            self.__coefficients[i] = self.__coefficients[i] / n

    