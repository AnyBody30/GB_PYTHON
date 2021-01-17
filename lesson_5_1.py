f = open('test.txt', 'w')
str = ' '
print('Вводите строки для вывода в файл:\n')
with f:
    while str != '\n':
        str = input() + '\n'
        f.write(str)
