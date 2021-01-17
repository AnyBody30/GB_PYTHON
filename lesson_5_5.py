from functools import reduce

f = open('test.txt', 'w', encoding="utf-8")
lst = []
str = ' '
# заполняем числами файл до ввода пустой строки
with f:
    while str != '':
        str = input('Введите число:')
        if str.isdigit():
            lst.append(str)
    f.write(' '.join(lst))

# считываем из файла и считаем сумму
f = open('test.txt', 'r', encoding="utf-8")
lst.clear()
summa = 0
with f:
    lst = f.read().split(' ')
    print('Сумма', reduce(lambda x, y: float(x)+float(y), lst))

