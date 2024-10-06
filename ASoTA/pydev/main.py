from asota import AsotaFacade
from users import Roles
from product import Product
from payment import SBP_Payment, CreditCardPayment, CashPayment

asota = AsotaFacade()
user = asota.add_user_to_system(Roles.trading_agent, "Vanya")
asota.enter_to_system(user=user)
# if you are warehouse manager
# here created product list for warehouse
product_list_of_warehouse = [
                [Product("Otvertka", 1.2), 2],
                [Product("Shurik", 30.1), 4],
                [Product("Molotok", 2), 10]
               ]
# only warehouse manager can edit items on wharehouse
asota.add_items_to_warehouse(product_list_of_warehouse)


# if you are trading agent
# ordered list forming by user request
ordered_list = [
                [Product("Otvertka", 1.2), 2],
                [Product("Shurik", 30.1), 1]
               ]

# only trading agent can create roder
asota.create_order( product_list=ordered_list,
                    customer_name="Bomj",
                    amount_from_cust=200, 
                    payment_type=SBP_Payment,
                    bank_name="sber"
                    )