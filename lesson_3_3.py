def my_func(a, b, c):
    return sum([a, b, c]) - min([a, b, c])


a, b, c = float(input('Введите аргумент 1: ')), float(input('Введите аргумент 2: ')), float(input('Введите аргумент 3: '))
print ('Сумма двух наибольших:', my_func(a, b, c))