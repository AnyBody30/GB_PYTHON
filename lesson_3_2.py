def PrintPersonalData (Name, Surname, BornYear, City, e_mail, phone):
    print(f'Имя: {Name}. Фамилия: {Surname}. Год рождения: {BornYear}. Город проживания: {City}. Электронная почта: {e_mail}. Телефон: {phone}.')
    return


PrintPersonalData(Name = input('Введите имя: '), Surname = input('Введите фамилию: '), BornYear = input('Введите год рождения: '), City = input('Введите город проживания: '), e_mail = input('Введите электронную почту: '), phone = input('Введите телефон: '))