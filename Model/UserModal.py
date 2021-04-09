import datetime


class User:
    def __init__(self, name, birth: datetime, cpf, email, pwd, active):
        self.name = name
        self.birth = birth
        self.cpf = cpf
        self.email = email
        self.pwd = pwd
        self.active = active(False)


