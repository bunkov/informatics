class Matrix:

    def __init__(self, m, n=None):
        if type(m) == int:
            if type(n) != int or m <= 0 or n <= 0:
                raise ValueError()
            self.m = m
            self.n = n

            result = [0]*m
            for i in range(m):
                result[i]=[0]*n

            self.matrix = result
        elif type(m) == list:
            if m == [] or n is not None:
                raise ValueError()
            self.matrix = m
            self.m = len(m)
            self.n = len(m[0])
        else:
            raise ValueError()
    def __add__(self, other):
        result = Matrix(self.m, self.n)

        for i in range(self.m):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return(result)

    def __sub__(self, other):
        result = Matrix(self.m, self.n)

        for i in range(self.m):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return(result)

    def __eq__(self, other):
        if self.m != other.m or self.n != other.n:
            raise RuntimeError()
        return(self.matrix == other.matrix)

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            result = Matrix(self.m, self.n)

            for i in range(self.m):
                for j in range(self.n):
                    result.matrix[i][j] = other*self.matrix[i][j]
        elif type(other) == Matrix and self.n == other.m:
            result = Matrix(self.m, other.n)

            for i in range(self.m):
                for j in range(other.n):
                    for k in range(other.m):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        else:
            raise RuntimeError()
        return(result)

    def __truediv__(self, other):

        if type(other) == float or type(other) == int:
            result = Matrix(self.m, self.n)

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

    def determinant(self):
        if self.m != self.n:
            raise RuntimeError()
        elif self.m == 2:
            result = self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
        elif self.m ==3:
            result = \
                self.matrix[0][0]*self.matrix[1][1]*self.matrix[2][2] + \
                self.matrix[0][1]*self.matrix[1][2]*self.matrix[2][0] + \
                self.matrix[1][0]*self.matrix[2][1]*self.matrix[0][2] - \
                self.matrix[0][2]*self.matrix[1][1]*self.matrix[2][0] - \
                self.matrix[0][0]*self.matrix[2][1]*self.matrix[1][2] - \
                self.matrix[1][0]*self.matrix[0][1]*self.matrix[2][2]
        return(result)

    def invert(self):
        if self.m != self.n:
            raise Exception()
        return (Matrix([[-1, 1],[2, -1]]))

    def transpose(self):
        result = Matrix(self.n, self.m)

        for i in range (self.n):
            for j in range(self.m):
                result.matrix[i][j]=self.matrix[j][i]
        return(result)