from ast import literal_eval

users = []
with open("Model/Users.txt", "r") as file:
    file = file.read()
    try:
        lista = literal_eval(file)
    except:
        raise Exception("Erro no banco de dados. Não foi possível converter ID.")
users = lista

class UserControl:

    def add_user(self, user, locale):
        if len(users) == 0:
            id = 1
        else:
            id = str(int(users[len(users) - 1]["id"]) + 1)
        users.append({"id": id,
                      "name": user.getname(),
                      "birth": user.getbirth(),
                      "cpf": user.getcpf(),
                      "email": user.getemail(),
                      "password": user.getpwd(),
                      "admin": user.getadmin()
                      })
        with open(locale, "w") as file:
            file.write(str(users))

    def get_users(self):
        return users

    def get_by_id(self, id):
        for i in range(len(users)):
            if users[i]["id"] == id:
                return users[i]
                break
        else:
            return []

    def get_by_email(self, email):
        for i in range(len(users)):
            if users[i]["email"] == email:
                return users[i]
                break
        else:
            return []

    def get_by_cpf(self, cpf):
        for i in range(len(users)):
            if users[i]["cpf"] == cpf:
                return users[i]
                break
        else:
            return []

    def update(self, user, locale):
        for i in range(len(users)):
            if users[i]["id"] == user.getid():
                if not user.getname() == users[i]["name"]:
                    users[i]["name"] = user.getname()
                if not user.getbirth() == users[i]["birth"]:
                    users[i]["birth"] = user.getbirth()
                if not user.getcpf() == users[i]["cpf"]:
                    users[i]["cpf"] = user.getcpf()
                if not user.getemail() == users[i]["email"]:
                    users[i]["email"] = user.getemail()
                if not user.getpwd() == users[i]["password"]:
                    users[i]["password"] = user.getpwd()
                if not user.getadmin() == users[i]["admin"]:
                    users[i]["admin"] = user.getadmin()
        with open(locale, "w") as file:
            file.write(str(users))