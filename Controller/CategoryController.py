from ast import literal_eval


class CategoryController():
    def add_category(self, category, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        if len(lista) == 0:
            id = 1
        else:
            id = str(int(lista[len(lista) - 1]["id"]) + 1)
        lista.append({"id": id,
                      "name": category.getname()
                      })
        with open(locale, "w") as file:
            file.write(str(lista))
    def get_categories(self, locale):
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
    def update(self, category, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        for i in range(len(lista)):
            if lista[i]["id"] == category.getid():
                if not lista[i]["name"] == category.getname():
                    lista[i]["name"] = category.getname()

        with open(locale, "w") as file:
            file.write(str(lista))
    def delete(self, id, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        for i in range(len(lista)):
            if lista[i]["id"] == id:
                lista.pop(i)
        with open(locale, "w") as file:
            file.write(str(lista))