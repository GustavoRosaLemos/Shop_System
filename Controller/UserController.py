from ast import literal_eval
from Model import UserModal
#UserModal.User()


class UserControl:
    # def __init__(self):
    #     super(UserController, self).__init__()

    def add_user(self):
        with open("../DatabaseController/Users.txt", "a") as file:
            if self.id > 0:
                file.write(str(self.id) + ";" + self.nome)

    def get_users(self):
        users = []
        with open("../DatabaseController/Users.txt", "r") as file:
            for user_file in file:
                user = tuple(user_file.strip().split(";"))
                users.append(user)
            file.read()
        return file

    def get_by_id(self):
        with open("../Model/Users.txt", "r") as file:
            file = file.read()
            ids = ""
            try:
               ids = literal_eval(file)

            except:
                raise Exception("Erro no banco de dados. Não foi possível converter ID.")
            return ids["usersid"]

    def update(self, id):
        with open("../DatabaseController/Users", "w") as file:
            file.read()
            try:
                id.file.literal_eval(file)
            except:
                raise Exception("Não foi possível atualizar.")

            return id["users"]