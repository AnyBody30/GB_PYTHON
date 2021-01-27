class Date:
    dt: str
    day: int
    month: int
    year: int

    def __init__(self, dt):
        Date.dt = dt

    @classmethod
    def date_trans(cls):
        lst = cls.dt.split('-')
        cls.day = int(lst[0])
        cls.month = int(lst[1])
        cls.year = int(lst[2])

    @staticmethod
    def date_validation():
        if Date.day < 1 or Date.day > 31:
            return False
        elif Date.month < 1 or Date.month > 12:
            return False
        elif Date.year < 1:
            return False
        else:
            return True


d = Date('24-09-1977')
Date.date_trans()
print(Date.date_validation())
