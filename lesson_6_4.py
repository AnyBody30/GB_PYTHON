class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Going...')

    def stop(self):
        print('Stopping...')

    def turn(self, direction):
        print(f'Turning to {direction}...')

    def show_speed(self):
        print(f'A Speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'A Speed is {self.speed}')
        if self.speed > 60:
            print('A Speed is over speedlimit...')


class WorkCar(Car):
    def show_speed(self):
        print(f'A Speed is {self.speed}')
        if self.speed > 40:
            print('A Speed is over speedlimit...')

tc = TownCar(70, 'Red', 'Volga', False)
print(tc.speed, tc.name, tc.color)
tc.go()
tc.stop()
tc.turn('Left')
tc.show_speed()

wc = WorkCar(30, 'Blue', 'Zil', False)
wc.show_speed()