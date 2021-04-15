class Car:
    def __init__(self, engine, body, wheels):
        self.engine = engine
        self.body = body
        self.wheels = wheels


class CarShowroom:
    def __init__(self, cars=[]):
        self.cars = cars
        #self.choice = choice

    def car_sale(self, choice):
        if choice == 'first car':
            self.cars.index(0)
        elif choice == 'second car':
            self.cars.index(1)
        elif choice == 'third car':
            self.cars.index(2)
        else:
            self.cars.index(3)
        return self.cars

    cars = ['first_car', 'second_car', 'third_car', 'fourth_car']


choice = input("Выберите машину(first car, second car, third car, fourth car): ")


sel = CarShowroom
print(sel.car_sale())
