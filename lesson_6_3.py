class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {'wage':wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Полный доход: {self._income.get("wage") +  self._income.get("bonus")}'


p = Position('Andrey', 'Ivanov', 1000, 700)
print(p.name)
print(p.surname)
print(p._income)
print(p.get_full_name())
print(p.get_total_income())