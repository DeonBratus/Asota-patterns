import product as prd
import warehouse as wrh

class OrderedProductList:

    def __init__(self) -> None:
        self.ordered_products = {}
    
    def add_item_to_list(self, product: prd.Product, q: int):
        if wrh.Warehouse._instance.is_available(product, q):
            if product.name in self.ordered_products:
                self.ordered_products[product.name]["quantity"] += q
                wrh.Warehouse._instance.items[product.name]["quantity"] -= q
            else:
                self.ordered_products[product.name] = {"quantity":q,"price": product.price, "desc": product.desc}
                wrh.Warehouse._instance.items[product.name]["quantity"] -= q
        else:
            print(f"Cannot add item {product.name}")

    