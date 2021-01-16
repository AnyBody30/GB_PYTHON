f = open('test.txt', 'r')
i = 0
with f:
    str = f.readline()
    while str != '':
        i += 1
        print(f'В {i}-й строке {len(str.split(" "))} слов')
        str = f.readline()
print(f'Всего в файле {i} строк.')
