from ast import literal_eval
from Model import UserModal
UserModal.User()

class UserController(UserModal):

    def __init__(self):
        super(UserController, self).__init__()

    def add_user(self):
        with open("../DatabaseController/Category.txt", "a") as file:
            if self.id > 0:
                file.write(str(self.id) + ";" + self.nome)

    def get_users(self):
        users = []
        with open("../DatabaseController/Category.txt", "r") as file:
            for user_file in file:
                user = tuple(user_file.strip().split(";"))
                users.append(user)
            file.read()
        return file

    def get_by_id(self):
        with open("../DatabaseController/Category.txt", "r") as file:
            for item in file:
                file.read(self.id)

                try:
                    literal_eval(file)

                except:
                    raise Exception("Erro no banco de dados. Não foi possível converter ID.")




    def update(self):


    def delete(self):
        pass

