
class Product:
    def __init__(self, name:str = "", price: float = 0) -> None:
        self._id: int = 12
        self.name = name
        self.desc = None
        self.price: int = price
    
    def set_price(self, price:float):
        self.price = price

    def set_desc(self, desc:str):
        self.desc = desc

    def show_info(self):
        print(f"ID {self._id}: {self.name}\nQnt: {self._quantity}, Price: {self.price}$\n\"{self.desc}\"")
