f = open('test.txt', 'r', encoding="utf-8")
result_dict = {}
with f:
    record = f.readline()
    # заменяем '-' чтобы потом их не ловить
    record = record.replace('—', '0(')
    lst = record.split(' ')
    while lst[0] != '':
        # собираем элемент словаря
        item_dict = {lst[0][0:-1]: int(lst[1][0: lst[1].index("(")]) + int(lst[2][0: lst[2].index("(")]) + int(lst[3][0: lst[3].index("(")])}
        # добавляем элекмент в результирующий словарь
        result_dict.update(item_dict)
        lst.clear()
        item_dict.clear()
        record = f.readline()
        record = record.replace('—', '0(')
        lst = record.split(' ')

print(result_dict)
