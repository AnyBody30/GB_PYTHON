class matrix:
    def __init__(self, mtrx):
        cl = len(mtrx[0])
        for i in range(0, len(mtrx)):
            if len(mtrx[i]) != cl:
                raise ValueError('В матрице строки должны быть одной размерности')
        self.data = mtrx

    def __str__(self):
        result = []
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                result.append(f'{str(self.data[x][y])} ')
            result.append('\n')
        return ''.join(result)

    def __add__(self, other):
        result = []
        item = []
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError('Складывать можно только матрицы одинаковых размерностей')
        for x in range(len(self.data)):
            item.clear()
            for y in range(len(self.data[x])):
                item.append(self.data[x][y] + other.data[x][y])
            result.append(list(item))
        return matrix(result)

mtrx1 = matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mtrx1)

mtrx2 = matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print(mtrx2)

mtrx3 = matrix([[21, 22, 23], [24, 25, 26], [27, 28, 29]])
print(mtrx3)

print(mtrx1 + mtrx2 + mtrx3)