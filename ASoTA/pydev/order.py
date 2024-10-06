import product_list as prl
import users 
import datetime

class OrderBuilder:
   
    def __init__(self) -> None:
        self.ordered_product_list = []
        self.total_amount = 0
        self.trading_agent_name = None
        self.order_customer = None
        self.time = None
        self.status = None
    
    def add_products(self, products: prl.OrderedProductList):
        for prod_key in products.ordered_products:
            self.ordered_product_list.append((prod_key, 
                                            products.ordered_products[prod_key]["quantity"],
                                            products.ordered_products[prod_key]["price"]))
        return self

    def compute_amount(self):
        for el in self.ordered_product_list:
            self.total_amount += el[2]*el[1]
        return self
    
    def set_trading_agent_name(self, user: users.User):
        self.trading_agent_name = user.name
        return self
    
    def set_order_customer_name(self, name:str):
        self.order_customer = name
        return self

    def set_time_order(self):
        self.time = datetime.datetime.now()
        return self
    
    def build(self):
        return Order(self)


class Order:
    def __init__(self, builder:OrderBuilder) -> None:
        self.product_list: prl.OrderedProductList = builder.ordered_product_list
        self.total_amount: float = builder.total_amount
        self.trading_agent_name: str = builder.trading_agent_name
        self.order_customer: str = builder.order_customer
        self.time = builder.time
        self.payment_status = None


    def show_order_info(self):
        # Заголовок чека
        print("========== Информация о заказе ==========")
        print(f"Торговый агент: {self.trading_agent_name}")
        print(f"Клиент: {self.order_customer}")
        print(f"Дата заказа: {self.time}")
        print("\nСписок товаров:")

        # Вывод списка товаров
        for prod in self.product_list:
            print(f"- {prod[0]} (Цена: {prod[2]} $.) - Количество: {prod[1]}")

        # Общая сумма
        print("\n-----------------------------------------")
        print(f"Общая сумма заказа: {self.total_amount} $.")
        print("=========================================")
        