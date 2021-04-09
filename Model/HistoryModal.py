class History:
    def __init__(self, client, product, price):
        self.client = client
        self.product = product
        self.price = price

    def get_client(self):
        return self.client

    def get_product(self):
        return self.product

    def get_price(self):
        return self.price

    def set_client(self, client):
        self.client = client

    def set_product(self, product):
        self.product = product

    def set_price(self, price):
        self.price = price
