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

class ProductController():
    def add_product(self, product, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        if len(lista) == 0:
            id = 1
        else:
            id = str(int(lista[len(lista) - 1]["id"]) + 1)
        lista.append({"id": id,
                      "name": product.getname(),
                      "price": product.getprice(),
                      "category": product.getcategory()
                      })
        with open(locale, "w") as file:
            file.write(str(lista))
    def get_products(self, locale):
        with open(locale, "r") as file:
            file = file.read()
            try:
                lista = literal_eval(file)
            except:
                raise Exception("Erro no banco de dados. Não foi possível converter ID.")
        return lista
    def get_by_id(self, id, locale):
        with open(locale, "r") as file:
            file = file.read()
            try:
                lista = literal_eval(file)
            except:
                raise Exception("Erro no banco de dados. Não foi possível converter ID.")
            for i in range(len(lista)):
                if lista[i]["id"] == id:
                    return lista[i]
                    break
            else:
                return []
    def update(self, product, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        for i in range(len(lista)):
            if lista[i]["id"] == product.getid():
                if not lista[i]["name"] == product.getname():
                    lista[i]["name"] = product.getname()
                if not lista[i]["price"] == product.getprice():
                    lista[i]["price"] = product.getprice()
                if not lista[i]["category"] == product.getcategory():
                    lista[i]["category"] = product.getcategory()

        with open(locale, "w") as file:
            file.write(str(lista))
    def delete(self, id, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        for i in range(len(lista)):
            if lista[i]["id"] == id:
                lista.pop(i)

    def buy(self, cart, user, card):
        from View import UserView
        print("cart = "+str(cart))
        for i in cart:
            print(i)
            if int(i["price"]) <= int(card["funds"]):
                from Controller import CardController
                CardController.cardcontrol().update(card["number"], i["price"], "Model/Cards.txt")
                print(f"{bcolors.OKGREEN}Compra de {i['name']} no valor de R${i['price']} realizada com sucesso!{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Falha na Compra: Você não possui saldo suficiente no cartão.{bcolors.ENDC}")
                UserView.main().showusercategorys(user)
        UserView.main().showusercategorys(user)