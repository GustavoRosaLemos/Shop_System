from View import HomeView
import string
import datetime


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
    def initialize(self):
        HomeView.main().showhome()
        HomeView.main().verifyhaslogin()

    def verifylogin(self, email, password):
        if email == "":
            print(f"{bcolors.FAIL}É necessario inserir um email!")
        if password == "":
            print(f"{bcolors.FAIL}É necessario inserir uma senha!")

        from Controller import UserController
        user = UserController.UserControl().get_by_email(email)
        if user == []:
            print(f"{bcolors.FAIL}O email ou a senha estão incorretos!{bcolors.ENDC}")
            HomeView.main().showlogin()
        if not user["email"] == email or not user["password"] == password:
            print(f"{bcolors.FAIL}O email ou a senha estão incorretos!{bcolors.ENDC}")
            HomeView.main().showlogin()



        if user["admin"] == True:
            from View import AdminView
            AdminView.main().showadminhome(user)
        else:
            from View import UserView
            UserView.main().showuserhome(user)

    def register(self, name, birth, cpf, email, password):
        from View import HomeView
        if name == "":
            print(f"{bcolors.FAIL}Seu nome não pode ser vazio!{bcolors.ENDC}")
            HomeView.main().showregister()
        if not " " in name:
            print(f"{bcolors.WARNING}Você deve inserir seu nome completo!{bcolors.ENDC}")
            HomeView.main().showregister()
        if len(name) <= 2:
            print(f"{bcolors.FAIL}Seu nome é muito pequeno!{bcolors.ENDC}")
            HomeView.main().showregister()
        for i in range(len(name)):
            if name[i] in string.digits:
                print(f"{bcolors.FAIL}Seu nome não pode possuir números!{bcolors.ENDC}")
                HomeView.main().showregister()
            elif not name[i] in string.ascii_letters and not name[i] == " ":
                print(f"{bcolors.FAIL}Seu nome não pode possuir caracteres especiais{bcolors.ENDC}")
                HomeView.main().showregister()
        if birth == "":
            print(f"{bcolors.FAIL}Sua data de nascimento não pode ser vazia!{bcolors.ENDC}")
            HomeView.main().showregister()
        if not "/" in birth:
            print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
            HomeView.main().showregister()

        for i in range(len(birth)):
            if birth[i] in string.ascii_letters:
                print(f"{bcolors.FAIL}Sua data de nascimento não pode conter letras!{bcolors.ENDC}")
                HomeView.main().showregister()
            elif not birth[i] in string.ascii_letters and not birth[i] == "/":
                pass

        if " " in birth:
            print(
                f"{bcolors.FAIL}Sua data de nascimento não pode conter espaços, formato correto (DD/MM/AAAA){bcolors.ENDC}")
            HomeView.main().showregister()
        sbirth = birth.split("/")
        if len(sbirth) > 3:
            print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
            HomeView.main().showregister()
        for i in range(3):
            if i == 0:
                if not len(sbirth[i]) == 2:
                    print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                    HomeView.main().showregister()
                if not int(sbirth[i]) >= 0 or not int(sbirth[i]) <= 31:
                    print(f"{bcolors.FAIL}Sua data de nascimento precisa estar entre 01 a 31 dias{bcolors.ENDC}")
                    HomeView.main().showregister()
            if i == 1:
                if not len(sbirth[i]) == 2:
                    print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                    HomeView.main().showregister()
                elif not int(sbirth[i]) >= 0 or not int(sbirth[i]) <= 12:
                    print(f"{bcolors.FAIL}Sua data de nascimento precisa estar entre 01 a 12 meses{bcolors.ENDC}")
                    HomeView.main().showregister()
            if i == 2:
                if not len(sbirth[i]) == 4:
                    print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                    HomeView.main().showregister()
                date = datetime.datetime.now()
                date = date.strftime('%Y')
                if not int(sbirth[i]) >= 1900 or not (int(sbirth[i]) <= int(date)):
                    print(f"{bcolors.FAIL}Sua data de nascimento precisa estar entre 1900 a {date} meses{bcolors.ENDC}")
                    HomeView.main().showregister()
        if cpf == "":
            print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
            HomeView.main().showregister()
        cpf = cpf.replace(".", "")
        cpf = cpf.replace("-", "")
        if not len(cpf) == 11:
            print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
            HomeView.main().showregister()
        isOnlySame = True
        for i in range(len(cpf)):
            if not i == 0:
                if not cpf[i] == cpf[i - 1]:
                    isOnlySame = False
            if not cpf[i] in string.digits:
                print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                HomeView.main().showregister()
        if isOnlySame:
            print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
            HomeView.main().showregister()
        numbers = [int(digit) for digit in cpf if digit.isdigit()]
        sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
            HomeView.main().showregister()
        sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
            HomeView.main().showregister()
        if email == "":
            print(f"{bcolors.FAIL}Você precisa inserir um endereço de email!{bcolors.ENDC}")
            HomeView.main().showregister()
        if not "@" in email:
            print(f"{bcolors.FAIL}O email inserido não é um email real!{bcolors.ENDC}")
            HomeView.main().showregister()
        if not "." in email:
            print(f"{bcolors.FAIL}O email insiredo não é um email real!{bcolors.ENDC}")
            HomeView.main().showregister()
        if " " in email:
            print(f"{bcolors.FAIL}O email não pode possuir espaços!{bcolors.ENDC}")
            HomeView.main().showregister()
        if password == "":
            print(f"{bcolors.FAIL}Você precisa inserir uma senha!{bcolors.ENDC}")
            HomeView.main().showregister()
        if " " in password:
            print(f"{bcolors.FAIL}A sua senha não pode possuir espaços!{bcolors.ENDC}")
            HomeView.main().showregister()
        if len(password) < 5:
            print(f"{bcolors.FAIL}A sua senha deve possuir pelo menos 5 caracteres!{bcolors.ENDC}")
            HomeView.main().showregister()

        from Model import UserModal
        from Controller import UserController

        if not UserController.UserControl().get_by_email(email) == []:
            print(f"{bcolors.FAIL}Já existe um usuario com esse email!{bcolors.ENDC}")
            HomeView.main().showregister()
        if not UserController.UserControl().get_by_cpf(cpf) == []:
            print(f"{bcolors.FAIL}Já existe um usuario com esse cpf!{bcolors.ENDC}")
            HomeView.main().showregister()
        try:
            UserController.UserControl().add_user(UserModal.User("0", name, birth, cpf, email, password, False), "Model/Users.txt")
            from View import HomeView
            HomeView.main().showlogin()
            print(f"{bcolors.OKGREEN}Usuário cadastrado com sucesso!{bcolors.ENDC}")
        except:
            print(f"{bcolors.WARNING}Não foi possível realizar o cadastro, tente novamente em alguns anos.{bcolors.ENDC}")