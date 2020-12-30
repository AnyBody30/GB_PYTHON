curresult = -1
while curresult <=0:
    curresult = float(input('Введите ненулевой результат пробежки первого дня: \n'))
targetresult = -1
while targetresult <=0:
    targetresult = float(input('Ведите ненулевой целевой результат: \n'))
daycounter = 1

# первый способ по формуле сложных процентов
import math
print('Первый способ. Ответ: на',math.ceil(math.log(targetresult/curresult, 1.1))+1,f'-й день спортсмен достиг результата - не менее {targetresult:} км.\n')

# второй способ иммитация процесса циклом
print(f'{daycounter}-й день: {curresult:.2f}')
while curresult < targetresult:
    daycounter = daycounter + 1
    curresult = curresult * 1.1
    print(f'{daycounter}-й день: {curresult:.2f}')
print (f'Второй способ. Ответ: на {daycounter}-й день спортсмен достиг результата - не менее {targetresult:} км.')