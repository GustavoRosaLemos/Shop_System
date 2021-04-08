import datetime


class User:
    def __init__(self, id, name, birth: datetime, cpf, email, pwd, active):
        self.id = id
        self.name = name
        self.birth = birth
        self.cpf = cpf
        self.email = email
        self.pwd = pwd
        self.active = active(False)


