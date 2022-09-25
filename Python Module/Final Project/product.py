class Product:
    products = []
    discount = 1

    def __init__(self, name, quantity, price, stock, discount=0):
        self.food_id = len(Product.products) + 1
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        Product.products.append(self)

    def edit_product(self, **product_data):
        if product_data["name"]:
            self.name = product_data["name"]
        if product_data["quantity"]:
            self.quantity = product_data["quantity"]
        if product_data["price"]:
            self.price = product_data["price"]
        if product_data["discount"]:
            self.discount = product_data["discount"]
        if product_data["stock"]:
            self.stock = product_data["stock"]

    def order_product(self):
        if self.stock <= 0:
            return False
        self.stock -= 1
        return True

    def get_product_data(self):
        food_data = {"name": self.name, "quantity": self.quantity, "price": self.price, "discount": self.discount,
                     "stock": self.stock}
        return food_data

    def remove_product(self):
        Product.products.pop(self.food_id - 1)
        Product.reset_all_food_ids()

    def __str__(self):
        return f"{self.food_id}. {self.name} ({self.quantity}) [INR {self.price}]"

    @classmethod
    def get_product(cls, food_id):
        if 0 < food_id <= len(cls.products):
            return cls.products[food_id - 1]
        else:
            return None

    @classmethod
    def get_all_products(cls):
        return cls.products

    @classmethod
    def get_all_products_data(cls):
        products_data = []
        for product in cls.products:
            products_data.append({"name": product.name, "quantity": product.quantity, "price": product.price,
                                  "discount": product.discount, "stock": product.stock})
        return products_data

    @classmethod
    def reset_all_food_ids(cls):
        for i, product in enumerate(cls.products):
            product.food_id = i + 1
