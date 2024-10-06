from product_list import OrderedProductList
from product import Product
from warehouse import Warehouse
from users import *
from order import OrderBuilder
from payment import *

class AsotaFacade:
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(AsotaFacade, cls).__new__(cls)
            cls.__instance.users = []
        return cls.__instance

    def __init__(self) -> None:
        self.warehouse = Warehouse()
        self.order_builder = OrderBuilder()
        self.__current_user: User
    
    def add_user_to_system(self, role, name):
        user = create_user(role, name)
        self.users.append(user)
        return user
    
    def enter_to_system(self, user: User):
        print(user in self.users)
        if user in self.users:
            print(f"Hello, {user.get_name()} you are {user.__class__.__name__}")
            self.__current_user = user
        else:
            return

    def create_new_product(self, name, price):
        product = Product(name, price)
        self.warehouse.edit_item(product, 0)
        return product
    
    # input_list[[Product, q], [Product, q]]
    def add_items_to_warehouse(self, items: list = []):
        for item in items:
            if item[0].name in self.warehouse.items:
                self.warehouse.items[item[0].name]["quantity"] = item[1]
            else:
                self.warehouse.edit_item(self.create_new_product(item[0].name, item[0].price), item[1])

    def __create_ordered_list(self, product_list: list):
        ordered_list = OrderedProductList()
        for prod in product_list:
            ordered_list.add_item_to_list(prod[0], prod[1])
        return ordered_list



    def create_order(self, product_list, customer_name: str, amount_from_cust, payment_type: PaymentStrategy, bank_name:str):
        ordered_list = self.__create_ordered_list(product_list=product_list)
        order = (self.order_builder
                 .add_products(products=ordered_list)
                 .compute_amount()
                 .set_trading_agent_name(self.__current_user)
                 .set_order_customer_name(customer_name)
                 .set_time_order()
                 .build()
                 )
        payment = PaymentContext(payment_type(bank_name))
        order.payment_status = payment.execute_context(amount_from_cust, order.total_amount)
        if order.payment_status == True:
            order.show_order_info()
        else:
            print(f"-----------------------\n|You don't have money!|\n-----------------------")
    
    
