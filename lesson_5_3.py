f = open('test.txt', 'r', encoding="utf-8")
lst = []
str = ' '
salary = 0
i = 0
print('Перечень струдников с доходом меньше 20000:')
with f:
    while True:
        str = f.readline()
        if str != '':
            sal = float(str.split(' ')[1][0:-1])
            if sal < 20_000:
                print(str.split(' ')[0], sal)
            salary = salary + sal
            i += 1
        else:
            break
if i > 0:
    print(f'\nСредний доход равен {salary/i}')
else:
    print('В файле нет данных')

#lst.sort(key = lambda x: float(x[1]))
#print(lst)