from ast import literal_eval

class cardcontrol:
    def add_card(self, card, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        lista.append({"number": card.get_number(),
                      "cvv": card.getccv(),
                      "date": card.getdate(),
                      "founds": card.getfunds()
                      })
        with open(locale, "w") as file:
            file.write(str(lista))

    def getcards(self, locale):
        with open(locale, "r") as file:
            file = file.read()
            try:
                lista = literal_eval(file)
            except:
                raise Exception("Erro no banco de dados. Não foi possível converter numero.")
        return lista

    def get_by_number(self, number, locale):
        with open(locale, "r") as file:
            file = file.read()
            try:
                lista = literal_eval(file)
            except:
                raise Exception("Erro no banco de dados. Não foi possível converter numero.")
            for i in range(len(lista)):
                if lista[i]["number"] == str(number):
                    return lista[i]
                    break
            else:
                return []

    def update(self, number, funds, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        for i in range(len(lista)):
            if lista[i]["number"] == number:
                intlista = int(lista[i]["funds"])
                intfunds = int(funds)
                intlista -= intfunds
                lista[i]["funds"] = str(intlista)



        with open(locale, "w") as file:
            file.write(str(lista))

    def delete(self, number, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        for i in range(len(lista)):
            if lista[i]["number"] == number:
                lista.pop(i)
        file = open(locale, "w")
        file.write(str(lista))
        file.close()