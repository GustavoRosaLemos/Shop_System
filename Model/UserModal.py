import datetime


class User:
    def __init__(self, id, name, birth, cpf, email, pwd, isAdmin):
        if not id == "0":
            self.id = id
        self.name = name
        self.birth = birth
        self.cpf = cpf
        self.email = email
        self.pwd = pwd
        self.isAdmin = isAdmin

    def setid(self, id):
        self.id = id

    def setname(self, name):
        self.name = name

    def setbirth(self, birth):
        self.birth = birth

    def setcpf(self, cpf):
        self.cpf = cpf

    def setemail(self, email):
        self.email = email

    def setpwd(self, pwd):
        self.pwd = pwd

    def setisadmin(self, isAdmin):
        self.isAdmin = isAdmin

    def getid(self):
        return self.id

    def getname(self):
        return self.name

    def getbirth(self):
        return self.birth

    def getcpf(self):
        return self.cpf

    def getemail(self):
        return self.email

    def getpwd(self):
        return self.pwd

    def getisAdmin(self):
        return self.isAdmin