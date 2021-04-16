class Vehicles(object):
    def __init__(self, engine, air_conditioner, central_locking, parm=[]):
        self.engine = engine
        self.air_conditioner = air_conditioner
        self.central_locking = central_locking
        self.parm = parm

    def v_parameters(self):
        v = "Мощность двигателя: {} h/p\nКондиционер: {}\nЦентральный замок: {}"\
            .format(self.engine, self.air_conditioner, self.central_locking)
        return v


class Sedan(Vehicles):
    def __init__(self, body, doors, drive_unit):
        self.air_conditioner = 'True'
        self.central_locking = 'True'
        self.engine = '200'
        self.body = body
        self.doors = doors
        self.drive_unit = drive_unit

    def v_parameters(self):
        s = "{}\nКузов: {}\nКол-во дверей: {}\n" \
            "Привод:{}".format(Vehicles.v_parameters(self), self.body, self.doors, self.drive_unit)
        return s


class Pickup(Vehicles):
    pass


class Sport(Vehicles):
    pass


vehicles = Vehicles('150', 'True', 'True')
sedan = Sedan('sedan', '4 doors', 'four-wheel drive')


print(Vehicles.v_parameters(vehicles))
print("*" * 30)
print(Sedan.v_parameters(sedan))
