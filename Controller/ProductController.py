from ast import literal_eval
import datetime

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

history = []
with open("Model/History.txt", "r") as file:
    file = file.read()
    hist = literal_eval(file)
history = hist

class ProductController():
    def add_product(self, product, locale):
        if len(products) == 0:
            id = 1
        else:
            id = int(products[len(products) - 1]["id"]) + 1
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
            if products[i]["id"] == id:
                products.pop(i)
                break
        with open(locale, "w") as file:
            file.write(str(products))
            file.close()

    def addhistory(self, cart, user, card, totalprice):
        history.append({"name": user['name'], "email": user['email'], "value": totalprice, "paymethod": "Cartão",
                        "number": card['number'], "itens": cart, "date": str(datetime.datetime.now())})
        with open("Model/History.txt", "w") as file:
            file.write(str(history))

    def addmoneyhistory(self, cart, user, totalprice):
        history.append({"name": user['name'], "email": user['email'], "value": totalprice, "paymethod": "Dinheiro", "number": "NONE", "itens": cart, "date": str(datetime.datetime.now())})
        with open("Model/History.txt", "w") as file:
            file.write(str(history))

    def gethistory(self):
        return history

    def buy(self, cart, user, card):
        from View import UserView
        totalprice = 0
        for i in cart:
            totalprice += float(i['price'])
        if totalprice <= float(card["funds"]):
            from Controller import CardController
            price = str(float(card["funds"]) - float(totalprice))
            CardController.cardcontrol().update(card["number"], price, "Model/Cards.txt")
            ProductController.addhistory(self, cart, user, card, totalprice)
            print(f"{bcolors.OKGREEN}Compra no valor de R${totalprice} realizada com sucesso!{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}Falha na Compra: Você não possui saldo suficiente no cartão.{bcolors.ENDC}")
            UserView.main().showusercategories(user)
        UserView.main().clearcart()
        UserView.main().showusercategories(user)

    def buymoney(self, cart, user):
        from View import UserView
        totalprice = 0
        for i in cart:
            totalprice += float(i['price'])
        print(f"Custo total: R${str(totalprice)}")
        payvalue = input("Digite o valor: R$")
        try:
            payvalue = float(payvalue)
        except:
            print(f"{bcolors.FAIL}O valor inserido é inválido!")
            ProductController.buymoney(self, cart, user)

        if totalprice <= payvalue:
            if payvalue <= 0:
                print(f"{bcolors.FAIL}O valor inserido é inválido!")
                ProductController.buymoney(self, cart, user)
            from Controller import CardController
            price = payvalue - float(totalprice)
            ProductController.addmoneyhistory(self, cart, user, totalprice)
            if price > 0:
                print(f"{bcolors.WARNING}Troco necessário: {price}{bcolors.ENDC}")
            print(f"{bcolors.OKGREEN}Compra no valor de R${totalprice} realizada com sucesso!{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}Falha na Compra: Você não possui saldo suficiente no cartão.{bcolors.ENDC}")
            UserView.main().showusercategories(user)
        UserView.main().clearcart()
        UserView.main().showusercategories(user)