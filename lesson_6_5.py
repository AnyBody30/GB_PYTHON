class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print ('Пишем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашем')

class Handle(Stationery):
    def draw(self):
        print('А вот и маркер подтянулся')


p = Pen('Ручка1')
p.draw()

pc = Pencil('Карандаш1')
pc.draw()

h = Handle('Маркер1')
h.draw()