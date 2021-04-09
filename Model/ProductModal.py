class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def setid(self, id):
        self.id = id

    def setname(self, name):
        self.name = name

    def setprice(self, price):
        self.price = price

    def setcategory(self, category):
        self.category = category

    def getid(self):
        return self.id

    def getname(self):
        return self.name

    def getprice(self):
        return self.price

    def getcategory(self):
        return self.category