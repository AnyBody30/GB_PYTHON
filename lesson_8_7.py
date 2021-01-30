class complex():
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __add__(self, other):
        return complex(self.Re + other.Re, self.Im + other.Re)

    def __sub__(self, other):
        return complex(self.Re - other.Re, self.Im - other.Re)

    def __mul__(self, other):
        return complex((self.Re * other.Re) + ((-1) * self.Im * other.Im), (self.Re * other.Im) + (other.Re * self.Im))

    def __truediv__(self, other):
        Re1 = self.Re
        Re2 = other.Re
        Im1 = self.Im
        Im2 = other.Im
        return complex((Re1 * Re2 + Im1 * Im2) / (Re2 * Re2 + Im2 * Im2), (Im1 * Re2 - Re1 * Im2) / ((Re2 * Re2 + Im2 * Im2)))

    def __str__(self):
        if self.Im == 0:
            return str(self.Re)
        elif self.Re == 0:
            return f'{self.Im}i'
        elif self.Im > 0:
            return f'{self.Re}+{self.Im}i'
        return f'{self.Re}{self.Im}i'

c1 = complex(-5, 6)
c2 = complex(3, -5)
c3 = complex(-7, -5)

print(c1 + c2 + c3)
print(c1 - c2 - c3)
print(c1 * c2 * c3)
print(c1 / c2 * c3 + c1 - c2)
print(complex(0, -4))
print(complex(2, 0))