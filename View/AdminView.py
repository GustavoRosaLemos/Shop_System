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
            main.usersoption(user)
        if selected < 0 or selected > 5:
            print(f"{bcolors.FAIL}Selecione uma opção válida!")
            main.usersoption(self, user)
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
                main.usersoption(self, user)

        elif selected == 2:
            from Controller import UserController
            print(f"\n{bcolors.BOLD}Insira o CPF do cliente que você deseja alterar.{bcolors.ENDC}\n")
            cpf = input("CPF: ")
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            editUser = UserController.UserControl().get_by_cpf(cpf)
            if not editUser:
                print(f"{bcolors.FAIL}Não foi possível encontrar um usuario com esse cpf!{bcolors.ENDC}")
                main.usersoption(self, user)
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
                main.usersoption(self, user)

        elif selected == 3:
            from Controller import UserController
            print(f"\n{bcolors.BOLD}Insira o CPF do cliente que você deseja remover.{bcolors.ENDC}\n")
            cpf = input("CPF: ")
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            remvUser = UserController.UserControl().get_by_cpf(cpf)
            if not remvUser:
                print(f"{bcolors.FAIL}Não foi possível encontrar um usuario com esse cpf!{bcolors.ENDC}")
            UserController.UserControl().delete(remvUser['cpf'], "Model/Users.txt")
            print(f"{bcolors.OKBLUE}Usuario removido com sucesso!")
            main.usersoption(self, user)
        elif selected == 4:
            from Controller import UserController
            list = UserController.UserControl().get_users()
            for i in list:
                print(f"{bcolors.BOLD}Nome:{bcolors.ENDC} {i['name']} {bcolors.BOLD}- Data de Nascimento:{bcolors.ENDC} {i['birth']} {bcolors.BOLD}- CPF:{bcolors.ENDC} {i['cpf']} {bcolors.BOLD}- Email:{bcolors.ENDC} {i['email']} {bcolors.BOLD}- Senha:{bcolors.ENDC} {i['password']} {bcolors.BOLD}- Admin:{bcolors.ENDC} {i['admin']}")
            input("\nPressione qualquer tecla para voltar...")
            main.usersoption(self, user)
        elif selected == 5:
            cpf = input("CPF: ")
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            from Controller import UserController
            result = UserController.UserControl().get_by_cpf(cpf)
            print(f"{bcolors.BOLD}Nome:{bcolors.ENDC} {result['name']} {bcolors.BOLD}- Data de Nascimento:{bcolors.ENDC} {result['birth']} {bcolors.BOLD}- CPF:{bcolors.ENDC} {result['cpf']} {bcolors.BOLD}- Email:{bcolors.ENDC} {result['email']} {bcolors.BOLD}- Senha:{bcolors.ENDC} {result['password']} {bcolors.BOLD}- Admin:{bcolors.ENDC} {result['admin']}")
            input("\nPressione qualquer tecla para voltar...")
            main.usersoption(self, user)

    def productsoptions(self, user):
        print(f"{bcolors.BOLD}Selecione uma opção:{bcolors.ENDC}")
        print("1 - Adicionar")
        print("2 - Modificar")
        print("3 - Remover")
        print("4 - Lista de Produtos")
        print("0 - Voltar")
        selected = input()
        try:
            selected = int(selected)
        except:
            print(f"{bcolors.FAIL}Selecione uma opção digitando o seu número.{bcolors.ENDC}")
            main.productsoptions(user)
        if selected < 0 or selected > 4:
            print(f"{bcolors.FAIL}Selecione uma opção válida!{bcolors.ENDC}")
            main.productsoptions(self, user)
        if selected == 0:
            main.showadmincategories(self, user)
        elif selected == 1:
            name = input("Nome: ")
            price = input("Valor: ")
            category = input("Categoria: ")

            if name == "":
                print(f"{bcolors.WARNING}É necessario que você adicione um nome ao produto!{bcolors.ENDC}")
                main.productsoptions(self, user)
            if price == "":
                print(f"{bcolors.WARNING}É necessario que você adicione um preço ao produto!{bcolors.ENDC}")
                main.productsoptions(self, user)
            if category == "":
                print(f"{bcolors.WARNING}É necessario que você adicione uma categoria ao produto!{bcolors.ENDC}")
                main.productsoptions(self, user)
            from Controller import ProductController
            from Controller import CategoryController
            try:
                category = int(category)
            except:
                print(f"{bcolors.FAIL}Você precisa insirir o ID da categoria.{bcolors.ENDC}")
                main.productsoptions(self, user)
            if not CategoryController.CategoryController().get_by_id(category):
                print(f"{bcolors.FAIL}Não foi possível localizar a categoria com esse ID!{bcolors.ENDC}")
                main.productsoptions(self, user)
            try:
                price = float(price)
                if price < 0:
                    print(f"{bcolors.FAIL}Você não pode colocar preços negativos!{bcolors.ENDC}")
                    main.productsoptions(self, user)
                price = str(price)
            except:
                print(f"{bcolors.FAIL}O valor do produto é inválido!{bcolors.ENDC}")
                main.productsoptions(self, user)
            else:
                from Model import ProductModal
                ProductController.ProductController().add_product(ProductModal.Product("0", name, price, category), "Model/Products.txt")
                print(f"{bcolors.OKGREEN}Produto adicionado com sucesso!{bcolors.ENDC}")
                main.productsoptions(self, user)
        elif selected == 2:
            resultid = input("ID do produto a ser alterado: ")
            from Controller import ProductController
            try:
                resultid = int(resultid)
            except:
                print(f"{bcolors.FAIL}Digite o número do ID do produto a ser pesquisado!{bcolors.ENDC}")
                main.productsoptions(self, user)
            result = ProductController.ProductController().get_by_id(resultid)
            print(f"{bcolors.BOLD}Não coloque nada nos campos que não deseja modificar.{bcolors.ENDC}")
            name = input("Nome: ")
            price = input("Valor: R$")
            category = input("Categoria: ")
            if not result:
                print(f"{bcolors.FAIL}Não foi possível localizar nenhum produto com esse ID.{bcolors.ENDC}")
                main.productsoptions(self, user)
            if name == "":
                name = result['name']
            if price == "":
                price = result['price']
            if category == "":
                category = result['category']
            if not result['name'] == name:
                result['name'] = name
            if not result['price'] == price:
                result['price'] = price
            if not result['category'] == category:
                result['category'] = category
            from Model import ProductModal
            ProductController.ProductController().update(ProductModal.Product(result['id'],result['name'], result['price'],
                                                                              result['category']), "Model/Products.txt")
            print(f"{bcolors.OKGREEN}Produto alterado com sucesso!{bcolors.ENDC}")
            main.productsoptions(self, user)
        elif selected == 3:
            remove = input("ID do produto a ser removido: ")
            try:
                remove = int(remove)
            except:
                print(f"{bcolors.WARNING}Digite o ID do produto que você deseja adicionar!")
                main.productsoptions(self, user)
            from Controller import ProductController
            result = ProductController.ProductController().get_by_id(remove)
            if not result:
                print(f"{bcolors.FAIL}Não foi possível localizar o produto a ser removido!")
                main.productsoptions(self, user)
            ProductController.ProductController().delete(remove, "Model/Products.txt")
            print(f"{bcolors.OKGREEN}Produto removido com sucesso!")
            main.productsoptions()
        elif selected == 4:
            from Controller import ProductController
            result = ProductController.ProductController().get_products()

            print(f"\n{bcolors.BOLD}Lista de Produtos:{bcolors.ENDC}")
            if not result:
                print("Vazio!")
            for i in range(len(result)):
                print(f"{bcolors.BOLD}ID: {bcolors.ENDC}{result[i]['id']}{bcolors.BOLD} - NOME:{bcolors.ENDC} {result[i]['name']}{bcolors.BOLD} - VALOR: {bcolors.ENDC}R${result[i]['price']}{bcolors.BOLD} - CATEGORIA:{bcolors.ENDC} {result[i]['category']}")
            input("Pressione ENTER para continuar...")
            main.productsoptions(self, user)

    def categoriesoptions(self, user):
        print(f"{bcolors.BOLD}Selecione uma opção:{bcolors.ENDC}")
        print("1 - Adicionar")
        print("2 - Remover")
        print("3 - Lista de Categorias")
        print("0 - Voltar")
        selected = input()
        try:
            selected = int(selected)
        except:
            print(f"{bcolors.FAIL}Selecione uma opção digitando o seu número.{bcolors.ENDC}")
            main.categoriesoptions(self, user)
        if selected < 0 or selected > 4:
            print(f"{bcolors.FAIL}Selecione uma opção válida!{bcolors.ENDC}")
            main.categoriesoptions(self, user)
        if selected == 0:
            main.showadmincategories(self, user)
        elif selected == 1:
            name = input("Nome: ")
            if name == "":
                print(f"{bcolors.FAIL}O nome da categoria não pode ser vazia!{bcolors.ENDC}")
                main.categoriesoptions(self, user)
            from Controller import CategoryController
            from Model import CategoryModal
            CategoryController.CategoryController().add_category(CategoryModal.Category(1, name), "Model/Category.txt")
            print(f"{bcolors.OKGREEN}Categoria adiconada com sucesso!{bcolors.ENDC}")
            main.categoriesoptions(self, user)
        elif selected == 2:
            from Controller import CategoryController
            remove = input("ID da categoria a ser removida: ")
            try:
                remove = int(remove)
            except:
                print(f"{bcolors.FAIL}Você precisa digitar o número do ID da categoria que deseja remover.")
                main.categoriesoptions(self, user)
            if not CategoryController.CategoryController().get_by_id(remove):
                print(f"{bcolors.FAIL}Não foi possível localizar a categoria")
                main.categoriesoptions(self, user)
            CategoryController.CategoryController().delete(remove, "Model/Category.txt")
            print(f"{bcolors.OKGREEN}Categoria removida com sucesso!")
            main.categoriesoptions(self, user)
        elif selected == 3:
            from Controller import CategoryController
            result = CategoryController.CategoryController().get_categories()
            for i in result:
                print(f"{bcolors.BOLD}ID:{bcolors.ENDC} {i['id']}{bcolors.BOLD} - NOME:{bcolors.ENDC} {i['name']}")
            input("Pressione ENTER para continuar...")
            main.categoriesoptions(self, user)

    def cardsoptions(self, user):
        print(f"{bcolors.BOLD}Selecione uma opção:{bcolors.ENDC}")
        print("1 - Adicionar")
        print("2 - Remover")
        print("3 - Lista de Cartões")
        print("0 - Voltar")
        selected = input()
        try:
            selected = int(selected)
        except:
            print(f"{bcolors.FAIL}Selecione uma opção digitando o seu número.{bcolors.ENDC}")
            main.cardsoptions(user)
        if selected < 0 or selected > 4:
            print(f"{bcolors.FAIL}Selecione uma opção válida!{bcolors.ENDC}")
            main.cardsoptions(self, user)
        if selected == 0:
            main.showadmincategories(self, user)
        elif selected == 1:
            number = input("Numero: ")
            if number == "":
                print(f"{bcolors.WARNING}O número do cartão não pode ser vazio!{bcolors.ENDC}")
                main.cardsoptions(self, user)
            from Controller import CardController
            if CardController.cardcontrol().get_by_number(number):
                print(f"{bcolors.WARNING}Já existe um cartão com esse número!{bcolors.ENDC}")
                main.cardsoptions(self, user)
            cvv = input("CVV: ")
            if cvv == "":
                print(f"{bcolors.WARNING}O CVV do cartão não pode ser vazio!{bcolors.ENDC}")
                main.cardsoptions(self, user)
            date = input("Data: (MM/AAAA) ")
            if date == "":
                print(f"{bcolors.WARNING}O data de validade do cartão não pode ser vazio!{bcolors.ENDC}")
                main.cardsoptions(self, user)
            datesplit = date.split("/")
            if not "/" in date:
                print(f"{bcolors.WARNING}A data de vencimento deve estar no formato (MM/AAAA).{bcolors.ENDC}")
                main.cardsoptions(self, user)
            if len(datesplit) > 2:
                print(f"{bcolors.WARNING}A data de vencimento deve estar no formato (MM/AAAA).{bcolors.ENDC}")
                main.cardsoptions(self, user)
            for i in range(len(datesplit)):
                if i == 0:
                    if not len(datesplit[i]) == 2:
                        print(f"{bcolors.WARNING}A data de vencimento deve estar no formato (MM/AAAA).{bcolors.ENDC}")
                        main.cardsoptions(self, user)
                elif i == 1:
                    if not len(datesplit[i]) == 4:
                        print(f"{bcolors.WARNING}A data de vencimento deve estar no formato (MM/AAAA).{bcolors.ENDC}")
                        main.cardsoptions(self, user)
            funds = input("Fundos: R$")
            try:
                float(funds)
            except:
                print(f"{bcolors.FAIL}O valor inserido nos fundos do cartão é inválido!.{bcolors.ENDC}")
                main.cardsoptions(self, user)
            from Model import CardModal
            CardController.cardcontrol().add_card(CardModal.Card(number, cvv, date, funds), "Model/Cards.txt")
            print(f"{bcolors.OKGREEN}Cartão adicionado com sucesso!{bcolors.ENDC}")
            main.cardsoptions(self, user)
        elif selected == 2:
            number = input("Numero do cartão a ser removido: ")
            from Controller import CardController
            result = CardController.cardcontrol().get_by_number(number)
            if not result:
                print(f"{bcolors.WARNING}Não foi possível localizar o cartão com esse número.{bcolors.ENDC}")
                main.cardsoptions(self, user)
            else:
                CardController.cardcontrol().delete(number, "Model/Cards.txt")
                print(f"{bcolors.OKGREEN}Cartão adicionado com sucesso!{bcolors.ENDC}")
                main.cardsoptions(self, user)
        elif selected == 3:
            from Controller import CardController
            result = CardController.cardcontrol().getcards()
            if not result:
                print("Não existe nenhum cartão cadastrado!")
            for i in result:
                print(f"{bcolors.BOLD}NÚMERO:{bcolors.ENDC} {i['number']}{bcolors.BOLD} - CVV:{bcolors.ENDC} {i['cvv']}{bcolors.BOLD} - DATA DE VALIDADE:{bcolors.ENDC} {i['date']}{bcolors.BOLD} - SALDO:{bcolors.ENDC} R${i['funds']}")
            input("Pressione ENTER para continuar...")
            main.cardsoptions(self, user)

    def showhistory(self, user):
        from Controller import ProductController
        result = ProductController.ProductController().gethistory()
        for i in result:
            if i['number'] == "NONE":
                print(f"{bcolors.BOLD}NOME:{bcolors.ENDC} {i['name']}{bcolors.BOLD} - EMAIL:{bcolors.ENDC} {i['email']}{bcolors.BOLD} - VALOR:{bcolors.ENDC} R${i['value']}{bcolors.BOLD} - METODO:{bcolors.ENDC} {i['paymethod']}{bcolors.BOLD} {i['number']}{bcolors.BOLD} - ITENS:{bcolors.ENDC} {str(i['itens'])} {bcolors.BOLD} DATA:{bcolors.ENDC} {i['date']}")
            else:
                print(f"{bcolors.BOLD}NOME:{bcolors.ENDC} {i['name']}{bcolors.BOLD} - EMAIL:{bcolors.ENDC} {i['email']}{bcolors.BOLD} - VALOR:{bcolors.ENDC} R${i['value']}{bcolors.BOLD} - METODO:{bcolors.ENDC} {i['paymethod']}{bcolors.BOLD} - CARTAO:{bcolors.ENDC} {i['number']}{bcolors.BOLD} - ITENS:{bcolors.ENDC} {str(i['itens'])} {bcolors.BOLD} DATA:{bcolors.ENDC} {i['date']}")
        if not result:
            print("Vazio!")
        input("Pressione ENTER para continuar...")
        main.showadmincategories(self, user)

    def showadmincategories(self, user):
        print(f"{bcolors.BOLD}Selecione uma opção:{bcolors.ENDC}")
        print(f"1 - Usuarios")
        print(f"2 - Produtos")
        print(f"3 - Categorias")
        print(f"4 - Cartões")
        print(f"5 - Historico de Vendas")
        print(f"0 - Sair")
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
            quit()
        elif selected == 1:
            main.usersoption(self, user)
        elif selected == 2:
            main.productsoptions(self, user)
        elif selected == 3:
            main.categoriesoptions(self, user)
        elif selected == 4:
            main.cardsoptions(self, user)
        elif selected == 5:
            main.showhistory(self, user)

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