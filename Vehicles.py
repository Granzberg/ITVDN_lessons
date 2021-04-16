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
            "Привод: {}".format(Vehicles.v_parameters(self), self.body, self.doors, self.drive_unit)
        return s


class Pickup(Vehicles):
    def __init__(self, trunk_volume, gearbox, body, doors, drive_unit):
        self.engine = '160'
        self.air_conditioner = 'True'
        self.central_locking = 'False'
        self.trunk_volume = trunk_volume
        self.gearbox = gearbox
        self.body = body
        self.doors = doors
        self.drive_unit = drive_unit

    def p_parameters(self):
        p = "{}\nОбьем багажника: {} l\nКаробка передеч: {}\nКузов: {}\nКол-во дверей: {}\nПривод: {}"\
            .format(Vehicles.v_parameters(self), self.trunk_volume, self.gearbox, self.body, self.doors, self.drive_unit)
        return p
    

class Sport(Vehicles):
    def __init__(self, body, drive_unit, spoiler, turbocharging):
        self.engine = '450'
        self.air_conditioner = 'False'
        self.central_locking = 'True'
        self.body = body
        self.drive_unit = drive_unit
        self.spoiler = spoiler
        self.turbocharging = turbocharging

    def sp_parameters(self):
        sp = "{}\nКузов: {}\nКаробка передеч: {}\nСпойлер: {}\nТурбонаддув: {}" \
            .format(Vehicles.v_parameters(self), self.body, self.drive_unit, self.spoiler, self.turbocharging,
                    self.drive_unit)
        return sp


vehicles = Vehicles('150', 'True', 'True')
sedan = Sedan('sedan', '4 doors', 'four-wheel drive')
pickup = Pickup('1060', 'five-speed gearbox', 'pickup', '2 doors', 'four-wheel drive')
sport = Sport('sport', 'five-speed gearbox', 'True', 'True')

print(Vehicles.v_parameters(vehicles))
print("*" * 30)
print(Sedan.v_parameters(sedan))
print("*" * 30)
print(Pickup.p_parameters(pickup))
print("*" * 30)
print(Sport.sp_parameters(sport))
