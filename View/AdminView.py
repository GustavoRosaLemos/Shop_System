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

import datetime
import string

class main:
    def usersoption(self, user):
        print(f"{bcolors.BOLD}Selecione uma opção:{bcolors.ENDC}")
        print("1 - Adicionar")
        print("2 - Modificar")
        print("3 - Remover")
        print("4 - Lista de Usuários")
        print("5 - Pesquisar")
        print("0 - Voltar")
        selected = input()
        try:
            selected = int(selected)
        except:
            print(f"{bcolors.FAIL}Selecione uma opção digitando o seu número.")
            main.showadmincategories(user)
        if selected < 0 or selected > 5:
            print(f"{bcolors.FAIL}Selecione uma opção válida!")
            main.showadmincategories(self, user)
        if selected == 0:
            main.showadmincategories(self, user)
        elif selected == 1:
            name = input("Nome: ")
            birth = input("Data de Nasciamento: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            password = input("Senha: ")
            admin = input("Admin(Sim/Não): ")

            if name == "":
               print(f"{bcolors.WARNING}O NOME não pode ser vazio!")
               main.usersoption(self, user)
            if birth == "":
                print(f"{bcolors.WARNING}A DATA DE NASCIMENTO não pode ser vazia!")
                main.usersoption(self, user)
            if cpf == "":
                print(f"{bcolors.WARNING}O CPF não pode ser vazio!")
                main.usersoption(self, user)
            if email == "":
                print(f"{bcolors.WARNING}O EMAIL não pode ser vazio!")
                main.usersoption(self, user)
            if password == "":
                print(f"{bcolors.WARNING}A SENHA não pode ser vazia!")
                main.usersoption(self, user)
            if not "/" in birth:
                print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                main.usersoption(self, user)

            for i in range(len(birth)):
                if birth[i] in string.ascii_letters:
                    print(f"{bcolors.FAIL}Sua data de nascimento não pode conter letras!{bcolors.ENDC}")
                    main.usersoption(self, user)
                elif not birth[i] in string.ascii_letters and not birth[i] == "/":
                    pass
            sbirth = birth.split("/")
            if len(sbirth) > 3:
                print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                main.usersoption(self, user)
            for i in range(3):
                if i == 0:
                    if not len(sbirth[i]) == 2:
                        print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                        main.usersoption(self, user)
                    if not int(sbirth[i]) >= 0 or not int(sbirth[i]) <= 31:
                        print(f"{bcolors.FAIL}Sua data de nascimento precisa estar entre 01 a 31 dias{bcolors.ENDC}")
                        main.usersoption(self, user)
                if i == 1:
                    if not len(sbirth[i]) == 2:
                        print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                        main.usersoption(self, user)
                    elif not int(sbirth[i]) >= 0 or not int(sbirth[i]) <= 12:
                        print(f"{bcolors.FAIL}Sua data de nascimento precisa estar entre 01 a 12 meses{bcolors.ENDC}")
                        main.usersoption(self, user)
                if i == 2:
                    if not len(sbirth[i]) == 4:
                        print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                        main.usersoption(self, user)
                    date = datetime.datetime.now()
                    date = date.strftime('%Y')
                    if not int(sbirth[i]) >= 1900 or not (int(sbirth[i]) <= int(date)):
                        print(f"{bcolors.FAIL}Sua data de nascimento precisa estar entre 1900 a {date} meses{bcolors.ENDC}")
                        main.usersoption(self, user)
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            if not len(cpf) == 11:
                print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                main.usersoption(self, user)
            isOnlySame = True
            for i in range(len(cpf)):
                if not i == 0:
                    if not cpf[i] == cpf[i - 1]:
                        isOnlySame = False
                if not cpf[i] in string.digits:
                    print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                    main.usersoption(self, user)
            if isOnlySame:
                print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                main.usersoption(self, user)
            numbers = [int(digit) for digit in cpf if digit.isdigit()]
            sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
            expected_digit = (sum_of_products * 10 % 11) % 10
            if numbers[9] != expected_digit:
                print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                main.usersoption(self, user)
            sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
            expected_digit = (sum_of_products * 10 % 11) % 10
            if numbers[10] != expected_digit:
                print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                main.usersoption(self, user)
            if " " in password:
                print(f"{bcolors.FAIL}A sua senha não pode possuir espaços!{bcolors.ENDC}")
                main.usersoption(self, user)
            if len(password) < 5:
                print(f"{bcolors.FAIL}A sua senha deve possuir pelo menos 5 caracteres!{bcolors.ENDC}")
                main.usersoption(self, user)
            if admin == "":
                admin = False
            elif admin.lower() == "sim" or admin.lower() == "sin" or admin.lower() == "s" or admin.lower() == "yes":
                admin = True
            else:
                admin = False

            from Model import UserModal
            from Controller import UserController

            if not UserController.UserControl().get_by_email(email) == []:
                print(f"{bcolors.FAIL}Já existe um usuario com esse email!{bcolors.ENDC}")
                main.usersoption(self, user)
            if not UserController.UserControl().get_by_cpf(cpf) == []:
                print(f"{bcolors.FAIL}Já existe um usuario com esse cpf!{bcolors.ENDC}")
                main.usersoption(self, user)
            try:
                UserController.UserControl().add_user(UserModal.User("0", name, birth, cpf, email, password, False),
                                                      "Model/Users.txt")
                from View import HomeView
                print(f"{bcolors.OKGREEN}Usuário cadastrado com sucesso!{bcolors.ENDC}")
                main.usersoption(self, user)
            except:
                print(f"{bcolors.WARNING}Não foi possível realizar o cadastro, tente novamente em alguns anos.{bcolors.ENDC}")

        elif selected == 2:
            from Controller import UserController
            print(f"\n{bcolors.BOLD}Insira o CPF do cliente que você deseja alterar.{bcolors.ENDC}\n")
            cpf = input("CPF: ")
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            editUser = UserController.UserControl().get_by_cpf(cpf)
            if not editUser:
                print(f"{bcolors.FAIL}Não foi possível encontrar um usuario com esse cpf!{bcolors.ENDC}")
            print(f"\n{bcolors.BOLD}Insira somente os dados que você deseja modificar!{bcolors.ENDC}\n")
            name = input("Nome: ")
            birth = input("Data de Nasciamento: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            password = input("Senha: ")
            admin = input("Admin(Sim/Não): ")

            if name == "":
                name = editUser["name"]
            if birth == "":
                birth = editUser["birth"]
            if cpf == "":
                cpf = editUser["cpf"]
            if email == "":
                email = editUser["email"]
            if password == "":
                password = editUser["password"]
            if not "/" in birth:
                print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                main.usersoption(self, user)

            for i in range(len(birth)):
                if birth[i] in string.ascii_letters:
                    print(f"{bcolors.FAIL}Sua data de nascimento não pode conter letras!{bcolors.ENDC}")
                    main.usersoption(self, user)
                elif not birth[i] in string.ascii_letters and not birth[i] == "/":
                    pass
            sbirth = birth.split("/")
            if len(sbirth) > 3:
                print(f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                main.usersoption(self, user)
            for i in range(3):
                if i == 0:
                    if not len(sbirth[i]) == 2:
                        print(
                            f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                        main.usersoption(self, user)
                    if not int(sbirth[i]) >= 0 or not int(sbirth[i]) <= 31:
                        print(f"{bcolors.FAIL}Sua data de nascimento precisa estar entre 01 a 31 dias{bcolors.ENDC}")
                        main.usersoption(self, user)
                if i == 1:
                    if not len(sbirth[i]) == 2:
                        print(
                            f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                        main.usersoption(self, user)
                    elif not int(sbirth[i]) >= 0 or not int(sbirth[i]) <= 12:
                        print(f"{bcolors.FAIL}Sua data de nascimento precisa estar entre 01 a 12 meses{bcolors.ENDC}")
                        main.usersoption(self, user)
                if i == 2:
                    if not len(sbirth[i]) == 4:
                        print(
                            f"{bcolors.FAIL}Sua data de nascimento precisa estar no formato (DD/MM/AAAA){bcolors.ENDC}")
                        main.usersoption(self, user)
                    date = datetime.datetime.now()
                    date = date.strftime('%Y')
                    if not int(sbirth[i]) >= 1900 or not (int(sbirth[i]) <= int(date)):
                        print(
                            f"{bcolors.FAIL}Sua data de nascimento precisa estar entre 1900 a {date} meses{bcolors.ENDC}")
                        main.usersoption(self, user)
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            if not len(cpf) == 11:
                print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                main.usersoption(self, user)
            isOnlySame = True
            for i in range(len(cpf)):
                if not i == 0:
                    if not cpf[i] == cpf[i - 1]:
                        isOnlySame = False
                if not cpf[i] in string.digits:
                    print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                    main.usersoption(self, user)
            if isOnlySame:
                print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                main.usersoption(self, user)
            numbers = [int(digit) for digit in cpf if digit.isdigit()]
            sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
            expected_digit = (sum_of_products * 10 % 11) % 10
            if numbers[9] != expected_digit:
                print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                main.usersoption(self, user)
            sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
            expected_digit = (sum_of_products * 10 % 11) % 10
            if numbers[10] != expected_digit:
                print(f"{bcolors.FAIL}CPF inválido!{bcolors.ENDC}")
                main.usersoption(self, user)
            if " " in password:
                print(f"{bcolors.FAIL}A sua senha não pode possuir espaços!{bcolors.ENDC}")
                main.usersoption(self, user)
            if len(password) < 5:
                print(f"{bcolors.FAIL}A sua senha deve possuir pelo menos 5 caracteres!{bcolors.ENDC}")
                main.usersoption(self, user)
            if admin == "":
                admin = False
            elif admin.lower() == "sim" or admin.lower() == "sin" or admin.lower() == "s" or admin.lower() == "yes":
                admin = True
            else:
                admin = False

            if not name == editUser["name"]:
                editUser["name"] = name
            if not birth == editUser["birth"]:
                editUser["birth"] = birth
            if not cpf == editUser["cpf"]:
                editUser["cpf"] = cpf
            if not email == editUser["email"]:
                editUser["email"] = email
            if not password == editUser["password"]:
                editUser["password"] = password
            if not admin == editUser["admin"]:
                editUser["admin"] = admin

            from Model import UserModal
            try:
                UserController.UserControl().update(
                    UserModal.User(editUser['id'], editUser['name'], editUser['birth'], editUser['cpf'],
                                   editUser['email'], editUser['password'], editUser['admin']), "Model/Users.txt")
                print(f"{bcolors.OKGREEN}Usuário alterado com sucesso!{bcolors.ENDC}")
                main.usersoption(self, user)
            except:
                print(f"{bcolors.WARNING}Não foi possível alterar o usuario, tente novamente em alguns anos.{bcolors.ENDC}")
        elif selected == 3:
            pass # rem
        elif selected == 4:
            pass # list
        elif selected == 5:
            pass # serach

    def showadmincategories(self, user):
        print(f"{bcolors.BOLD}Selecione uma opção:{bcolors.ENDC}")
        print(f"1 - Usuarios")
        print(f"2 - Produtos")
        print(f"3 - Categorias")
        print(f"4 - Cartões")
        print(f"0 - Sair")
        selected = input()
        try:
            selected = int(selected)
        except:
            print(f"{bcolors.FAIL}Selecione uma opção digitando o seu número.")
            main.showadmincategories(user)
        if selected < 0 or selected > 4:
            print(f"{bcolors.FAIL}Selecione uma opção válida!")
            main.showadmincategories(self, user)
        if selected == 0:
            quit()
        elif selected == 1:
            main.usersoption(self, user)
        elif selected == 2:
            pass
        elif selected == 4:
            pass

    def showadminhome(self, user):
        print("-" * 187)
        print(("\t" * 10) + f"{bcolors.OKCYAN} __        ______      _____   ______          ______   __    __  __        ______  __    __  ________ {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}|  \      /      \    |     \ /      \        /      \ |  \  |  \|  \      |      \|  \  |  \|        \ {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     |  $$$$$$\    \$$$$$|  $$$$$$\      |  $$$$$$\| $$\ | $$| $$       \$$$$$$| $$\ | $$| $$$$$$$${bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     | $$  | $$      | $$| $$__| $$      | $$  | $$| $$$\| $$| $$        | $$  | $$$\| $$| $$__    {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     | $$  | $$ __   | $$| $$    $$      | $$  | $$| $$$$\ $$| $$        | $$  | $$$$\ $$| $$  \   {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     | $$  | $$|  \  | $$| $$$$$$$$      | $$  | $$| $$\$$ $$| $$        | $$  | $$\$$ $$| $$$$$   {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$_____| $$__/ $$| $$__| $$| $$  | $$      | $$__/ $$| $$ \$$$$| $$_____  _| $$_ | $$ \$$$$| $$_____ {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     \ $$    $$ \$$    $$| $$  | $$       \$$    $$| $$  \$$$| $$     \|   $$ \| $$  \$$$| $$     \ {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN} \$$$$$$$$ \$$$$$$   \$$$$$$  \$$   \$$        \$$$$$$  \$$   \$$ \$$$$$$$$ \$$$$$$ \$$   \$$ \$$$$$$$${bcolors.ENDC}")


        print(f'{bcolors.OKGREEN}Olá ADMIN {user["name"]}, seja bem vindo!\n{bcolors.ENDC}')
        main.showadmincategories(self, user)