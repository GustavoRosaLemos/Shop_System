from Controller import HomeController


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class main:
    def verifyhaslogin(self):
        print(f"{bcolors.BOLD}Bem vindo, você possui cadastro?{bcolors.ENDC}")
        hasLogin = input("(Sim/Não): ")

        if hasLogin.lower() == "s" or hasLogin.lower() == "sim" or hasLogin.lower() == "sin" or hasLogin.lower() == "si" or hasLogin.lower() == "yes":
            main.showlogin(self)
        elif hasLogin.lower() == "n" or hasLogin.lower() == "nao" or hasLogin.lower() == "não" or hasLogin.lower() == "na" or hasLogin.lower() == "no":
            main.showregister(self)
        else:
            main.verifyhaslogin(self)


    def showhome(self):
        print("-"*187)
        print(("\t"*10) + f"{bcolors.OKCYAN} __        ______      _____   ______          ______   __    __  __        ______  __    __  ________ {bcolors.ENDC}")
        print(("\t"*10) + f"{bcolors.OKCYAN}|  \      /      \    |     \ /      \        /      \ |  \  |  \|  \      |      \|  \  |  \|        \ {bcolors.ENDC}")
        print(("\t"*10) + f"{bcolors.OKCYAN}| $$     |  $$$$$$\    \$$$$$|  $$$$$$\      |  $$$$$$\| $$\ | $$| $$       \$$$$$$| $$\ | $$| $$$$$$$${bcolors.ENDC}")
        print(("\t"*10) + f"{bcolors.OKCYAN}| $$     | $$  | $$      | $$| $$__| $$      | $$  | $$| $$$\| $$| $$        | $$  | $$$\| $$| $$__    {bcolors.ENDC}")
        print(("\t"*10) + f"{bcolors.OKCYAN}| $$     | $$  | $$ __   | $$| $$    $$      | $$  | $$| $$$$\ $$| $$        | $$  | $$$$\ $$| $$  \   {bcolors.ENDC}")
        print(("\t"*10) + f"{bcolors.OKCYAN}| $$     | $$  | $$|  \  | $$| $$$$$$$$      | $$  | $$| $$\$$ $$| $$        | $$  | $$\$$ $$| $$$$$   {bcolors.ENDC}")
        print(("\t"*10) + f"{bcolors.OKCYAN}| $$_____| $$__/ $$| $$__| $$| $$  | $$      | $$__/ $$| $$ \$$$$| $$_____  _| $$_ | $$ \$$$$| $$_____ {bcolors.ENDC}")
        print(("\t"*10) + f"{bcolors.OKCYAN}| $$     \ $$    $$ \$$    $$| $$  | $$       \$$    $$| $$  \$$$| $$     \|   $$ \| $$  \$$$| $$     \ {bcolors.ENDC}")
        print(("\t"*10) + f"{bcolors.OKCYAN} \$$$$$$$$ \$$$$$$   \$$$$$$  \$$   \$$        \$$$$$$  \$$   \$$ \$$$$$$$$ \$$$$$$ \$$   \$$ \$$$$$$$${bcolors.ENDC}")
        print(("\t" * 16) + f"{bcolors.WARNING}Onde coisas inuteis são vendidas por preços absurdos!{bcolors.ENDC}")


    def showlogin(self):
        print(f"\n{bcolors.BOLD}Digite os dados a baixo para realizar o login.{bcolors.ENDC}")
        email = input("Email: ")
        password = input("Senha: ")
        HomeController.main().verifylogin(email, password)


    def showregister(self):
        print(f"\n{bcolors.BOLD}Digite os dados a baixo para realizar o cadastro.{bcolors.ENDC}")
        name = input("Nome Completo: ")
        birth = input("Data de Nascimento (DD/MM/AAAA): ")
        cpf = input("CPF: ")
        email = input("Email: ")
        password = input("Senha: ")
        HomeController.main().register(name, birth, cpf, email, password)