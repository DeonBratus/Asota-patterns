import product as prd

class Warehouse:
    _instance = None

    # singleton. Can be created only one object of warehouse class
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Warehouse, cls).__new__(cls)
        return cls._instance
    

    def __init__(self):
        # {product.name : {"quantity": q, "price": product.price, "desc": product.desc}}
        self.items = {}


    def edit_item(self, product: prd.Product, quantity):
        if product.name in self.items:
            self.items[product.name]["quantity"] += quantity
        else:
            self.items[product.name] = {"quantity":quantity,"price": product.price, "desc": product.desc}
    
    def is_available(self, product: prd.Product, quant):
        return self.items[product.name]["quantity"] >= quant
