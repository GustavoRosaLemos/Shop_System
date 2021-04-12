from ast import literal_eval

categories = []
with open("Model/Category.txt", "r") as file:
    file = file.read()
    try:
        lista = literal_eval(file)
    except:
        raise Exception("Erro no banco de dados. Não foi possível converter ID.")
categories = lista

class CategoryController():
    def add_category(self, category, locale):
        if len(categories) == 0:
            id = 1
        else:
            id = int(categories[len(categories) - 1]["id"]) + 1
        categories.append({"id": id,
                      "name": category.getname()
                      })
        with open(locale, "w") as file:
            file.write(str(categories))
            file.close()

    def get_categories(self):
        return categories

    def get_by_id(self, id):
        for i in range(len(categories)):
            if categories[i]["id"] == id:
                return categories[i]
                break
        else:
            return []

    def update(self, category, locale):
        for i in range(len(categories)):
            if categories[i]["id"] == category.getid():
                if not categories[i]["name"] == category.getname():
                    categories[i]["name"] = category.getname()

        with open(locale, "w") as file:
            file.write(str(categories))
            file.flush()

    def delete(self, id, locale):
        for i in range(len(categories)):
            if categories[i]["id"] == id:
                categories.pop(i)
                break
        with open(locale, "w") as file:
            file.write(str(categories))
            file.flush()