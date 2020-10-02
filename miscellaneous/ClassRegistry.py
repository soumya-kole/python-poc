_registry = {}


class MetaClass(type):
    def __init__(cls, clsname, bases, methods):
        super().__init__(clsname, bases, methods)
        _registry[cls.__name__] = cls


class CAR(metaclass=MetaClass):

    def __str__(self):
        return "This is a car"


class BUS(metaclass=MetaClass):

    def __str__(self):
        return "This is a bus"


class TRAIN(metaclass=MetaClass):

    def __str__(self):
        return "This is a train"


def create_vehicle(vehicle_type):
    target_class = vehicle_type.upper()
    return _registry[target_class]()


vehicles = ['bus', 'car', 'train']
for v in vehicles:
    print (create_vehicle(v))
