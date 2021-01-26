class clothes:
    name = 'Одежда'

    def cloth_consuption(self):
        pass



class coat(clothes):
    name = 'Пальто'

    def __init__(self, size):
        self.size = size

    @property
    def cloth_consuption(self):
        return self.size / 6.5 + 0.5



class suit(clothes):
    name = 'Костюм'

    def __init__(self, growth):
        self.growth = growth

    @property
    def cloth_consuption(self):
        return 2 * self.growth + 0.3


cc = coat(52)
sc = suit(5)

print(f'Расход ткани на пальто и костюм составляет: {cc.cloth_consuption + sc.cloth_consuption}')