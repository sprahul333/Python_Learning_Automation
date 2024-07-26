from abc import abstractmethod


class ABC:

    @abstractmethod
    def abc(self):
        pass


class DEF(ABC):

    def abc(self):
        print("Abstract method")
        return "Abstract Method"

obj=DEF()

obj.abc()

print("********************************************************************************************************************************************")

# from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for vehicles"""

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start(self):
        """Abstract method to start the vehicle"""
        pass

    @abstractmethod
    def stop(self):
        """Abstract method to stop the vehicle"""
        pass

class Car(Vehicle):
    """Concrete subclass for cars"""

    def start(self):
        print(f"Starting the {self.make} {self.model} car.")

    def stop(self):
        print(f"Stopping the {self.make} {self.model} car.")

class Motorcycle(Vehicle):
    """Concrete subclass for motorcycles"""

    def start(self):
        print(f"Starting the {self.make} {self.model} motorcycle.")

    def stop(self):
        print(f"Stopping the {self.make} {self.model} motorcycle.")

# Creating instances of concrete subclasses
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "CBR600RR")

# Calling the abstract methods
car.start()    # Output: Starting the Toyota Camry car.
car.stop()     # Output: Stopping the Toyota Camry car.
motorcycle.start()  # Output: Starting the Honda CBR600RR motorcycle.
motorcycle.stop()   # Output: Stopping the Honda CBR600RR motorcycle.

