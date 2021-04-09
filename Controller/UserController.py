from ast import literal_eval
from Model import UserModal
#UserModal.User()


class UserControl:
    # def __init__(self):
    #     super(UserController, self).__init__()

    def add_user(self, user, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        if len(lista) == 0:
            id = 1
        else:
            id = str(int(lista[len(lista) - 1]["id"]) + 1)
        lista.append({"id": id,
                      "name": user.getname(),
                      "birth": user.getbirth(),
                      "cpf": user.getcpf(),
                      "email": user.getemail(),
                      "password": user.getpwd(),
                      "admin": user.getadmin()
                      })
        with open("Model/Users.txt", "w") as file:
            file.write(str(lista))

    def get_users(self, locale):
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

    def update(self, user, locale):
        with open(locale, "r") as file:
            file = file.read()
            lista = literal_eval(file)
        for i in range(len(lista)):
            if lista[i]["id"] == user.getid():
                if not user.getname() == lista[i]["name"]:
                    lista[i]["name"] = user.getname()
                if not user.getbirth() == lista[i]["birth"]:
                    lista[i]["birth"] = user.getbirth()
                if not user.getcpf() == lista[i]["cpf"]:
                    lista[i]["cpf"] = user.getcpf()
                if not user.getemail() == lista[i]["email"]:
                    lista[i]["email"] = user.getemail()
                if not user.getpwd() == lista[i]["password"]:
                    lista[i]["password"] = user.getpwd()
                if not user.getadmin() == lista[i]["admin"]:
                    lista[i]["admin"] = user.getadmin()
        with open(locale, "w") as file:
            file.write(str(lista))