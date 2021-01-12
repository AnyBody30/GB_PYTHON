from functools import reduce

def fact(n):
    for i in range(1, n+1):
        yield reduce(lambda x, y: x*y, range(1, i+1))


n = int(input('Введите до какого числа вычислять факториалы: '))
for el in fact(n):
    print(el)
