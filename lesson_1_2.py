time_in_sec = int(input('Введите время в секундах:\n'))
# если ввели число секунд больше чем в сутках, то целые сутки откидываем и оставляем остаток секунд в пределах суток
if time_in_sec > 86400:
    time_in_sec = time_in_sec % 86400
print(f'Время: {time_in_sec // 3600:02}:{time_in_sec % 3600 // 60:02}:{time_in_sec % 3600 % 60:02}')
