class MyZeroDivisionException(Exception):
    def __init__(self, description):
        self.description = description


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
try:
    if b == 0:
        raise MyZeroDivisionException('Обычно на ноль делить нельзя...')
    else:
        print(a/b)
except MyZeroDivisionException as err:
    print(err)
