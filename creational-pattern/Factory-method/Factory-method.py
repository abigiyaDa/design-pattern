# core idea 
# Move object creation into a method that can be overridden.

# step -1 : Product Interface
# - declares the interface, which is common to all objects that can be produced by the creator and its subclasses.


from abc import ABC, abstractmethod


class Transport(ABC):
    """Product interface"""
    @abstractmethod
    def deliver(self) -> str:
        pass 

# Step 2: Concrete Products

class Truck(Transport):
    def deliver(self) -> str:
        return "Delivering cargo by land in a truck."


class Ship(Transport):
    def deliver(self) -> str:
        return "Delivering cargo by sea in a ship."
    
# Step 3: Creator (Base Logistics Class)

class Logistics(ABC):
    """
    Creator class.
    Contains business logic that relies on Transport objects.
    """

    @abstractmethod
    def create_transport(self) -> Transport:
        """Factory Method"""
        pass

    def plan_delivery(self) -> str:
        """
        Core business logic.
        It doesn't know what concrete transport it gets.
        """
        transport = self.create_transport()
        return f"Logistics: Planning delivery... {transport.deliver()}"
    
# Step 4: Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()
    
# Step 5: Client Code
def client_code(logistics: Logistics):
    print(logistics.plan_delivery())


if __name__ == "__main__":
    print("App: Using Road Logistics")
    client_code(RoadLogistics())

    print("\nApp: Using Sea Logistics")
    client_code(SeaLogistics())