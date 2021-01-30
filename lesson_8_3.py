class MyException(Exception):
    def __init__(self, description):
        self.description = description


ls = []

while True:
    try:
        item = input('Введите число в список: ')
        if item == 'stop':
            break
        if item.isdigit():
            ls.append(float(item))
        else:
            raise MyException('Вводить надо только числа...')
    except MyException as err:
        print(err)
print(ls)
