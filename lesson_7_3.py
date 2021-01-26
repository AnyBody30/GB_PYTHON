class Cell:
    def __init__(self, qnt):
        self.quantity = int(qnt)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        else:
            raise ValueError('Нельзя вычесть из меньшей клетки большую')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, row_qnt):
        lst = []
        for i in range(1, self.quantity // row_qnt + 1):
            lst.append(f'{"*" * int(row_qnt)}\n')
        lst.append(f'{"*" * int(self.quantity % row_qnt)}\n')
        return ''.join(lst)

    def __str__(self):
        return f'Количество клеток: {self.quantity}'


c1 = Cell(87)
c2 = Cell(15)
c3 = Cell(17)
c4 = c1 + c2 + c3
print(c4)
c5 = c4 * c3
print(c5)
c6 = c5 / c3
print(c6)
c7 = c6 - c2
print(c7)
print(c7.make_order(17))