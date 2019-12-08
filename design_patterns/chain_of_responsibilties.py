class Car(object):

    def __init__(self, name, water, fuel, oil):
        self.name = name
        self.water = water
        self.fuel = fuel
        self.oil = oil

    def is_fine(self):
        if self.water >= 20 and self.fuel >= 5 and self.oil >= 10:
            print('Car {} is good to go'.format(self.name))
            return True
        else:
            return False

    def __str__(self):
        return "[Name: " + self.name + " Water: " + str(self.water) + " Fuel: " + str(self.fuel) + "]"


class Handler(object):

    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, car):
        if not car.is_fine() and self._successor is not None:
            self._successor.handle_request(car)


class WaterHandler(Handler):

    def handle_request(self, car):
        if car.water < 20:
            car.water = 100
            print('Added water')
            super(WaterHandler, self).handle_request(car)


class FuelHandler(Handler):

    def handle_request(self, car):
        if car.fuel < 5:
            car.fuel = 100
            print('Added fuel')
        super(FuelHandler, self).handle_request(car)


class OilHandler(Handler):

    def handle_request(self, car):
        if car.oil < 10:
            car.oil = 100
            print('Added oil')
        super(OilHandler, self).handle_request(car)


if __name__ == '__main__':
    my_car = Car("my car", 1, 2, 3)
    your_car = Car("your car", 1, 20, 30)
    mechanic = WaterHandler(FuelHandler(OilHandler()))
    mechanic.handle_request(my_car)
    mechanic.handle_request(your_car)

