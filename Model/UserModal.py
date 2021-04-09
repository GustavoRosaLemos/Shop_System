import datetime


class User:
    def __init__(self, name, birth, cpf, email, pwd, isAdmin):
        self.name = name
        self.birth = birth
        self.cpf = cpf
        self.email = email
        self.pwd = pwd
        self.isAdmin = isAdmin


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






