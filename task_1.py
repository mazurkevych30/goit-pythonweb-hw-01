from abc import ABC, abstractmethod
from logger import logger


class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make: str = make
        self.model: str = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info("%s %s : Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info("%s %s : Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(f"{make} (EU Spec)", model)


# Usage for US Vehicles
us_factory = USVehicleFactory()
us_car = us_factory.create_car("Toyota", "Corolla")
us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

us_car.start_engine()
us_motorcycle.start_engine()

# Usage for EU Vehicles
eu_factory = EUVehicleFactory()
eu_car = eu_factory.create_car("Toyota", "Corolla")
eu_motorcycle = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")

eu_car.start_engine()
eu_motorcycle.start_engine()
