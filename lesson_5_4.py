f = open('test.txt', 'r', encoding="utf-8")
fr = open('result.txt', 'w', encoding="utf-8")
dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with f, fr:
    str = f.readline()
    while str !='':
        lst = str.split('-')
        fr.write(f'{dic.get(lst[0])}-{lst[1]}')
        str = f.readline()