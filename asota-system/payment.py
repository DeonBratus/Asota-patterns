from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PaymentStatus:
    no_payment = False
    falled_payment = False
    successful_payment = True

class CreditCardPayment(PaymentStrategy):

    def __init__(self, bank_name) -> None:
        super().__init__()
        self.bank_name = bank_name
        self.__card_number = None

    def pay(self, amount):
        print(f"Payment {amount} with credit card {self.bank_name}")


class SBP_Payment(PaymentStrategy):

    def __init__(self, bank_name) -> None:
        super().__init__()
        self.bank_name = bank_name
        self.__phone = None
    
    def pay(self, amount):
        print(f"Payment {amount} with SBP {self.bank_name}")
    

class CashPayment(PaymentStrategy):

    def __init__(self) -> None:
        super().__init__()
    
    def pay(self, amount):
        print(f"Payemnt {amount} with money")

class PaymentContext:

    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy
        self.status = PaymentStatus.no_payment

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy
    
    def execute_context(self, payment_amount, prods_amount):
        if payment_amount >= prods_amount:
            self._strategy.pay(amount=payment_amount)
            self.status = PaymentStatus.successful_payment
        else:
            self.status = PaymentStatus.falled_payment

        return self.status
