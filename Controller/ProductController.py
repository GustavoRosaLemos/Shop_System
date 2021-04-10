from ast import literal_eval

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

products = []
with open("Model/Products.txt", "r") as file:
    file = file.read()
    try:
        lista = literal_eval(file)
    except:
        raise Exception("Erro no banco de dados. Não foi possível converter ID.")
products = lista

class ProductController():
    def add_product(self, product, locale):
        if len(products) == 0:
            id = 1
        else:
            id = str(int(products[len(products) - 1]["id"]) + 1)
        products.append({"id": id,
                      "name": product.getname(),
                      "price": product.getprice(),
                      "category": product.getcategory()
                      })
        with open(locale, "w") as file:
            file.write(str(products))

    def get_products(self):
        return products

    def get_by_id(self, id):
        for i in range(len(products)):
            if products[i]["id"] == id:
                return products[i]
                break
        else:
            return []

    def update(self, product, locale):
        for i in range(len(products)):
            if products[i]["id"] == product.getid():
                if not products[i]["name"] == product.getname():
                    products[i]["name"] = product.getname()
                if not products[i]["price"] == product.getprice():
                    products[i]["price"] = product.getprice()
                if not products[i]["category"] == product.getcategory():
                    products[i]["category"] = product.getcategory()
        with open(locale, "w") as file:
            file.write(str(products))

    def delete(self, id, locale):
        for i in range(len(products)):
            if products[i]["number"] == products:
                products.pop(i)
        with open(locale, "w") as file:
            file.write(str(products))
            file.close()

    def buy(self, cart, user, card):
        from View import UserView
        for i in cart:
            if float(i["price"]) <= float(card["funds"]):
                from Controller import CardController
                price = str(float(card["funds"]) - float(i["price"]))
                CardController.cardcontrol().update(card["number"], price, "Model/Cards.txt")
                print(f"{bcolors.OKGREEN}Compra de {i['name']} no valor de R${i['price']} realizada com sucesso!{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Falha na Compra: Você não possui saldo suficiente no cartão.{bcolors.ENDC}")
                UserView.main().showusercategorys(user)
        UserView.main().clearcart()
        UserView.main().showusercategorys(user)