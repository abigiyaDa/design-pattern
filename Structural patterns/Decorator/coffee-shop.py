# step 1 component interface 
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# step 2 concrete component
class BasicCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Basic Coffee"
    
# step 3 decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()
    
# step 4 concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Milk"
    
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", Sugar"
    

# step 5 use the decorators
if __name__ == "__main__":
    basic_coffee = BasicCoffee()
    print(f"{basic_coffee.description()} costs ${basic_coffee.cost()}")

    milk_coffee = MilkDecorator(basic_coffee)
    print(f"{milk_coffee.description()} costs ${milk_coffee.cost()}")

    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print(f"{sugar_milk_coffee.description()} costs ${sugar_milk_coffee.cost()}")


# output:
# Basic Coffee costs $5
# Basic Coffee, Milk costs $7
# Basic Coffee, Milk, Sugar costs $8