class Road:
    __depth = 0
    __unit_weigth = 0

    def get_mass(self):
        pass



class Asphalt_Road(Road):
    __depth = 13
    __unit_weigth = 31

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self):
        return self._length * self._width * self.__depth * self.__unit_weigth


ar = Asphalt_Road(7000, 7)
print(f'Требуемая масса асфальта: {ar.get_mass()} кг.')