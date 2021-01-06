string = input('Введите предложение из нескольких слов, раделяя слова пробелами:\n')
str_lst = string.split(' ')
for i in range(len(str_lst)):
    if len(str_lst[i]) <= 10:
        print(f'{i} {str_lst[i]}')
    else:
        print(f'{i} {str_lst[i][:10]}')