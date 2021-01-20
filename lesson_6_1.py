from itertools import cycle
from time import sleep

class TrafficLight:

    def __init__(self, r_duration, y_duration, g_duration):
        self.__color_dic = {'Red': r_duration, 'Yellow': y_duration, 'Green': g_duration}
        self.__color = ''

    def running(self, next_color):
            self.__color = next_color
            sleep(self.__color_dic.get(next_color))

    def get_color(self):
        return self.__color




tl = TrafficLight(7, 2, 5)
# бесконечно переключаем светофор
print('TrafficLight is running...')
for x in cycle(['Red', 'Yellow', 'Green']):
    tl.running(x)
    print(tl.get_color())