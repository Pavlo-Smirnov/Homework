class Product:

    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.type}): {self.price}$"

class StoreProduct(Product):

    def __init__(self, type_, name, price):
        self.sell_price = price * 1.3
        super().__init__(type_, name, price)

    def __repr__(self):
        return f"{self.name} ({self.type}): {self.sell_price}$"

class ProductStore:


    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product: Product, amount: int):
        new_product = StoreProduct(product.type, product.name, product.price)
        self.products[new_product.name] = {"product": new_product, "amount": amount}

    def set_discount(self, identifier: str, percent: int, identifier_type='name'):
        if 100 < percent < 0:
            raise ValueError("Percent can be between 0 and 100")
        if not isinstance(identifier, str):
            raise TypeError("Identifier must be str")

        if identifier_type == 'name':
            self.products[identifier]["product"].price *= (0.01 * percent)

        elif identifier_type == "type":
            for name, product in self.products.items():
                print(product)
                if product["product"].type == identifier:
                    product["product"].sell_price *= (0.01 * percent)
        else:
            raise ValueError("Identifier can be 'name' or 'type'")

    def sell_product(self, product_name, amount):
        if amount < 0 or amount > self.products[product_name]["amount"]:
            raise ValueError("Wrong amount")
        sell_product = self.products[product_name]["product"]

        self.products[product_name]["amount"] -= amount
        self.income += (sell_product.sell_price - sell_product.price) * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        return self.products[product_name]

store = ProductStore()
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

store.add(p, 10)
store.add(p2, 300)
print(store.products)
store.set_discount('Sport', 50, "type")
print(store.products)
store.sell_product("Ramen", 20)
print(store.products)
print(store.get_income())
print(store.get_all_products())
print(store.get_product_info("Football T-Shirt"))