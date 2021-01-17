import json

f = open('test.txt', 'r', encoding="utf-8")
result_dict = {}
sum_profit = 0
i = 0
with f:
    record = f.readline()
    lst = record.split(' ')
    while lst[0] !='':
        profit = float(lst[2]) - float(lst[3])
        # считаем общую прибыль и количество прибыльных компаний
        if profit > 0:
            sum_profit = sum_profit + profit
            i += 1
        # собираем элемент словаря с названием фирмы и прибыли (убытки)
        item_dict = {lst[0]: profit}
        # добавляем элекмент в результирующий словарь
        result_dict.update(item_dict)
        lst.clear()
        item_dict.clear()
        record = f.readline()
        lst = record.split(' ')
item_dict = {'average_profit': (sum_profit / i)}
result_dict.update(item_dict)
print(result_dict)

f = open('tesult.json', 'w', encoding="utf-8")
with f:
    json.dump(result_dict, f)
