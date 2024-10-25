from abc import ABC, abstractmethod

class User:


    def __init__(self,user_id: int = 0, name: str = None) -> None:
        self.name: str = name
        self.user_id: int = user_id
        self.phone: str = None
        self.email: str = None

    def get_name(self) -> str:
        return self.name
    

    def get_phone(self) -> str:
        return self.phone
    

    def work(self): 
        print("I'm working. I don't now what i'm doing")


class TradingAgent(User):


    def __init__(self, user_id: int = 0, name: str = None) -> None:
        super().__init__(user_id, name)
        self.point_of_sales_address = None
    

    def work(self):
        print(f"{self.name} is selling")
    

    def createOrder(self, func_action: callable):
        print(f"Order is ready on store by {self.name} with address: {self.point_of_sales_address}\n")


class WarehouseManager(User):


    def __init__(self, user_id: int = 0, name: str = None) -> None:
        super().__init__(user_id, name)
        self.list_of_supply_company = {}
    

    def work(self):
        print(f"{self.name} is working on warehouse")


    def getSupply(self):
        print(f"{self.name} got supply from", *self.list_of_supply_company["Bolt&Gaika"], "\n")


class StoreOwner(User):


    def __init__(self, user_id: int = 0, name: str = None) -> None:
        super().__init__(user_id, name)
    

    def work(self):
        print(f"{self.name} working maybe")


    def fixation_pribil(self):
        print(f"{self.name} is fixing pribil'")


class Roles:
    trading_agent = 0
    warehouse_manager = 1
    shop_owner = 2

# Used fabric method. this function choose class of creating object
def create_user(role: Roles, name: str):
    if role == Roles.trading_agent:
        return TradingAgent(name=name)
    elif role == Roles.warehouse_manager:
        return WarehouseManager(name=name)
    elif role == Roles.shop_owner:
        return StoreOwner(name=name)