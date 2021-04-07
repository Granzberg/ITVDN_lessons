class Temperature:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def to_celsius(self):
        return (self.temperature - 32) / 1.8

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


human = Temperature(37)


print(human.temperature)

print(human.to_fahrenheit())

human = Temperature()

print(human.to_celsius())

coldest_thing = Temperature(-270)
