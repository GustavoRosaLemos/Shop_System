from ast import literal_eval


class ProductController():


    def add_product(self, product):
        with open("Model/Products.txt", "r") as file:
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
        with open("Model/Products.txt", "w") as file:
            file.write(str(lista))
    def get_products(self):
        pass
    def get_by_id(self):
        pass
    def uptade(self):
        pass
    def delete(self):
        pass