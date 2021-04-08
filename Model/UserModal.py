class User:
    def __init__(self, name, age, cpf, email, pwd, active):
        self.name = name
        self.age = age
        self.cpf = cpf
        self.email = email
        self.pwd = pwd
        self.active = active(False)


