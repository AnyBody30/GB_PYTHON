def degree (x, y):
    return x ** y

def negative_degree (x, y):
    b = 1.0
    for i in range(abs(y)):
        b = b * x
    return 1 / b

x = 0
while x <= 0:
    x = float(input('Введите действительное положительное число: '))
y = 0
while y >= 0:
    y = int(input('Введите целое отрицательное число: '))

print (f'Возведение {x} в степень {y} встроенными средствами: ', degree (x, y))
print (f'Возведение {x} в степень {y} через цикл: ', negative_degree(x, y))