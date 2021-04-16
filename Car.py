class Car:
    def __init__(self, engine, body, wheels, cars=[]):
        self.engine = engine
        self.body = body
        self.wheels = wheels
        self.cars = cars

    def __str__(self):
        s = "\nМошность двигателя: {}\nКузов:              {}\nРежим хода:         {}"\
            .format(self.engine, self.body, self.wheels)
        return s


class CarShowroom:
    def __init__(self, text):
        self.text = text

    def car_sale(self):
        if choice == 'first car':
            print(Car.__str__(first_car))
        elif choice == 'second car':
            print(Car.__str__(second_car))
        elif choice == 'third car':
            print(Car.__str__(third_car))
        elif choice == 'fourth car':
            print(Car.__str__(fourth_car))


first_car = Car('250 h/p', 'sedan', 'city')
second_car = Car('500 h/p', 'R-class', 'city')
third_car = Car('350 h/p', 'sport_sedan', 'city')
fourth_car = Car('250 h/p', 'jeep', '4x4')

choice = input("Выберите машину(first car, second car, third car, fourth car): ")
sel = CarShowroom
sel.car_sale(choice)
