def division (a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

try:
    x = float(input('Введите делимое: '))
    y = float(input('Введите делитель: '))
except ValueError:
    print('Необходимо было ввести числа, а не буквенные символы')
else:
    print('Частное:', division(x, y))
