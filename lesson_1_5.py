revenue = -1
while revenue < 0:
    revenue = float(input('Введите значение выручки, положительное число:\n'))
costs = -1
while costs < 0:
    costs = float(input('Введите значение издержек, положительное число:\n'))
if revenue > costs:
    profit = (revenue - costs)/revenue
    print(f'Компания прибыльная. Рентабельность составляет {profit:.2f}\n')
    pe = (revenue-costs)/int(input('Введите количество сотрудников компании:\n'))
    print(f'Прибыль в расчете на одного сотрудника составляет: {pe:.2f}')
elif revenue < costs:
    print('Компания убыточная.\n')
else:
    print('Компания безубыточная.\n')
