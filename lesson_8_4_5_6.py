from abc import ABC, abstractmethod

class NoEqpInStoreEx(Exception):
    def __init__(self, description):
        self.description = description

class ErrTypeParamEqpEx(Exception):
    def __init__(self, description):
        self.description = description

class Equipment(ABC):
    def __init__(self, id, weigth, place, vendor, model, sn):
        if type(id) is int:
            self.id = id
        else:
            raise ErrTypeParamEqpEx('Идентификатор оборудования должен быть целым числом')
        if type(weigth) is float or type(weigth) is int:
                self.weigth = weigth
        else:
            raise ErrTypeParamEqpEx('Вес оборудования должен быть числом')
        self.place = place
        self.vendor = vendor
        self.model = model
        self.sn = sn
        self.status = 'purchased'
        self.type = ''

    def store_entering(self, place):
        self.place = place
        self.status = 'entered'

    def store_removing(self, place):
        self.place = place
        self.status = 'distributed'


class Printer(Equipment):
    def __init__(self, id, weigth, storeid, vendor, model, sn, cartridgetype):
        super().__init__(id, weigth, storeid, vendor, model, sn)
        self.cartridgetype = cartridgetype
        self.type = 'Printer'


class Scanner(Equipment):
    def __init__(self, id, weigth, storeid, vendor, model, sn, resolution):
        super().__init__(id, weigth, storeid, vendor, model, sn)
        self.resolution = resolution
        self.type = 'Scanner'


class Copier(Equipment):
    def __init__(self, id, weigth, storeid, vendor, model, sn, copy_speed):
        super().__init__(id, weigth, storeid, vendor, model, sn)
        self.copy_speed = copy_speed
        self.type = 'Copier'


class StoreHouse():

    def __init__(self, store_name):
        self.store_name = store_name
        self.nomenclature = {}


    def enter(self, eqp: Equipment):
        eqp.store_entering(self.store_name)
        if self.nomenclature.get(eqp.type):
            self.nomenclature.update({eqp.type: {'quantity': self.nomenclature.get(eqp.type).get('quantity') + 1, 'weigth': self.nomenclature.get(eqp.type).get('weigth') + eqp.weigth}})
        else:
            self.nomenclature.update({eqp.type: {'quantity': 1, 'weigth': eqp.weigth}})

    def removal(self, eqp: Equipment, deparment_name):
        eqp.store_removing(deparment_name)
        if self.nomenclature.get(eqp.type) and self.nomenclature.get(eqp.type).get('quantity') > 0:
            self.nomenclature.update({eqp.type: {'quantity': self.nomenclature.get(eqp.type).get('quantity') - 1, 'weigth': self.nomenclature.get(eqp.type).get('weigth') - eqp.weigth}})
        else:
            raise NoEqpInStoreEx(f'Оборудования типа {eqp.type} нет на складе')


try:
    p = Printer(1, 5, 4, 1, 8, 9, 90)
    sc = Scanner(7, 8, 4, 1, 8, 9, 90)
    s = StoreHouse('MainStore')
    s.enter(p)
    s.enter(sc)
    print(s.nomenclature)

    p1 = Printer(3, 8, 4, 1, 8, 9, 90)
    sc1 = Scanner(2, 9, 4, 1, 8, 9, 90)
    s.enter(p1)
    s.enter(sc1)
    print(s.nomenclature)

    s.removal(p1, 'Accountant dep')
    s.removal(sc1, 'Sales dep.')
    print(s.nomenclature)

except NoEqpInStoreEx as err:
    print(err)
except ErrTypeParamEqpEx as err:
    print(err)
