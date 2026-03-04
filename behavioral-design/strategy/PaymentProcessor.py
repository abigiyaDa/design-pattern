#  step 1 define the strategy interface 

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

# Step 2: Implement Concrete Strategies

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self,amount):
        print(f"Paid {amount} using paypal")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount ):
        print(f"Paid {amount} using bitcoin")

# Step 3: Create the Context

class PaymentProcessor:
    def __init__(self, strategy : PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy : PaymentStrategy): 
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)

# Step 4: Use the Strategy
if __name__ == "__main__":
    processor = PaymentProcessor(CreditCardPayment())
    processor.pay(100)

    processor.set_strategy(PayPalPayment())
    processor.pay(200)

    processor.set_strategy(BitcoinPayment())
    processor.pay(300)


# output:
# Paid 100 using Credit Card
# Paid 200 using paypal
# Paid 300 using bitcoin    

