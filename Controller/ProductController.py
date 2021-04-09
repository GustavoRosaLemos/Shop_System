from ast import literal_eval


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