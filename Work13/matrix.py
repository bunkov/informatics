

class Matrix:

    def __init__(self, m, n=None):
        if type(m) == int:
            self.m = m
            self.n = n

            result = [0]*m
            for i in range(m):
                result[i]=[0]*n

            self.matrix = result
        elif type(m) == list:
            self.matrix = m

    def __add__(self, other):
        result = Matrix(self.m, self.n)
        result.matrix = [0]*self.m
        for i in range(self.m):
            result.matrix[i]=[0]*self.n

        for i in range(self.m):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return(result)

    def __sub__(self, other):
        result = Matrix(self.m, self.n)
        result.matrix = [0]*self.m
        for i in range(self.m):
            result.matrix[i]=[0]*self.n

        for i in range(self.m):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return(result)

    def __eq__(self, other):
        return(self.matrix == other.matrix)

    def __mul__(self, other):

        if type(other) == float or type(other) == int:
            result = Matrix(self.m, self.n)
            result.matrix = [0]*self.m
            for i in range(self.m):
                result.matrix[i]=[0]*self.n

            for i in range(self.m):
                for j in range(self.n):
                    result.matrix[i][j] = other*self.matrix[i][j]
        elif type(other) == Matrix and self.n == other.m:
            result = Matrix(self.m, other.n)
            result.matrix = [0]*self.m
            for i in range(self.m):
                result.matrix[i]=[0]*other.n

            for i in range(self.m):
                for j in range(other.n):
                    for k in range(other.m):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return(result)

    def __truediv__(self, other):

        if type(other) == float or type(other) == int:
            result = Matrix(self.m, self.n)
            result.matrix = [0]*self.m
            for i in range(self.m):
                result.matrix[i]=[0]*self.n

            for i in range(self.m):
                for j in range(self.n):
                    result.matrix[i][j] = self.matrix[i][j]/other
        return(result)

    def get(self, i, j):
        return(self.matrix[i][j])

    def get_m(self):
        return(self.m)

    def get_n(self):
        return(self.n)

    def get_size(self):
        return(self.m,self.n)

    def set(self, i, j, value):
        self.matrix[i][j] = value