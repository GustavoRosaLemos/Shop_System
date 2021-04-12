import random

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
cart = []
class main:
    def putcard(self, user, cart):
        print(f"{bcolors.BOLD}Insida os dados do seu cartão:{bcolors.ENDC}")
        number = input("Numero: ")
        cvv = input("cvv: ")
        date = input("Data: ")
        if number == "":
            print(f"{bcolors.FAIL}Você precisa inserir o numero do cartão!{bcolors.ENDC}")
            main.putcard(self, user, cart)
        if cvv == "":
            print(f"{bcolors.FAIL}Você precisa inserir o numero do cvv!{bcolors.ENDC}")
            main.putcard(self, user, cart)
        if date == "":
            print(f"{bcolors.FAIL}Você precisa inserir o numero de vencimento do cartão!{bcolors.ENDC}")
            main.putcard(self, user, cart)

        from Controller import CardController
        card = CardController.cardcontrol().get_by_number(number)
        if not card:
            print(f"{bcolors.FAIL} O cartão que você inseriu não existe!{bcolors.ENDC}")
            main.putcard(self, user, cart)

        if not card['cvv'] == cvv and not card['date'] == date:
            print(f"{bcolors.FAIL} Os dados do cartão que você inseriu não estão corretos!{bcolors.ENDC}")
            main.putcard(self, user, cart)

        from Controller import ProductController
        ProductController.ProductController().buy(cart, user, card)

    def clearcart(self):
        global cart
        cart = []

    def selectpaymethod(self, user):
        print("1 - Cartão")
        print("2 - Dinheiro")
        print("0 - Voltar")
        selected = input("")

        try:
            selected = int(selected)
        except:
            print(f"{bcolors.FAIL}Selecione uma opção válida!{bcolors.ENDC}")
            main.showusercategories(self, user)

        if selected == 0:
            main.showusercategories(self, user)
        elif selected == 1:
            main.putcard(self, user, cart)
        elif selected == 2:
            from Controller import ProductController
            ProductController.ProductController().buymoney(cart, user)

    def showuserproducts(self, user, category):
        print(f"{bcolors.BOLD}Selecione um produto:{bcolors.ENDC}")
        from Controller import ProductController
        products = ProductController.ProductController().get_products()
        print(f"{bcolors.WARNING} EXISTEM {random.randint(1000000, 9999999999999999999999)} USUARIOS INTERESSADOS NO PRODUTO QUE VOCÊ ESTÁ VENDO AGORA!{bcolors.ENDC}")
        print(f"{bcolors.WARNING} !!!!50% OFF!!!! VOCÊ TEM 5 SEGUNDOS PARA APROVEITAR A PROMOÇÃO EXCLUSIVA!{bcolors.ENDC}")
        for i in range(len(products)):
            if products[i]['category'] == category:
                print(f"{i+1} - {products[i]['name']} - {bcolors.OKGREEN}R${products[i]['price']}{bcolors.ENDC}")
        print("0 - Voltar")

        product = input("")
        try:
            product = int(product)
        except:
            main.showuserproducts(self, user, category)
        if product == 0:
            main.showuserhome(self, user)
        if not product >= 1 and not product <= len(products):
            print(f"{bcolors.WARNING}Selecione um produto válido!{bcolors.ENDC}")
            main.showusercategories()
        product = products[product - 1]
        global cart
        cart.append(product)
        another = input("Continuar Comprando: ")
        if another.lower() == "sim" or another.lower() == "sin" or another.lower() == "si" or another.lower() == "s" or another.lower() == "yes":
            main.showusercategories(self, user)
        main.selectpaymethod(self, user)

    def cartremovequestion(self, user):
        response = input("Deseja remover algum item? (Sim/Não) ")
        if response.lower() == "sim" or response.lower() == "s" or response.lower() == "sin" or response.lower() == "si" or response.lower() == "yes":
            for i in range(len(cart)):
                print(f"{bcolors.BOLD}ID: {bcolors.ENDC}{i}{bcolors.BOLD} - NOME:{bcolors.ENDC} {cart[i]['name']}{bcolors.BOLD} - VALOR: {bcolors.ENDC}R${cart[i]['price']}")
            response = input("Digite o ID que deseja remover: ")
            if response == "":
                main.showusercategories()
            try:
                response = int(response)
            except:
                print(f"{bcolors.FAIL}Resposta inválida! Digite o número do item que deseja remover.{bcolors.ENDC}")
                main.cartremovequestion(self, user)
            if not cart:
                print(f"{bcolors.WARNING}Você não possui itens no carrinho.{bcolors.ENDC}")
                main.showusercategories(self, user)
            if response >= 0 and response <= len(cart):
                cart.pop(response)
                print(f"{bcolors.OKGREEN}Item removido com sucesso!{bcolors.ENDC}")
                main.cartremovequestion(self, user)
        elif response.lower() == "n" or response.lower() == "não" or response.lower() == "nao" or response.lower() == "na":
            main.cartcompletequestion(self, user)
        else:
            print(f"{bcolors.FAIL}Resposta inválida! Responda com sim ou não{bcolors.ENDC}")
            main.cartremovequestion(self, user)

    def cartcompletequestion(self, user):
        response = input("Deseja finaliza a compra? (Sim/Não) ")
        if response.lower() == "sim" or response.lower() == "s" or response.lower() == "sin" or response.lower() == "si" or response.lower() == "yes":
            main.putcard(self, user, cart)
        elif response.lower() == "n" or response.lower() == "não" or response.lower() == "nao" or response.lower() == "na":
            main.showusercategories(self, user)
        else:
            print(f"{bcolors.FAIL}Resposta inválida! Responda com sim ou não{bcolors.ENDC}")
            main.cartcompletequestion(self, user)

    def showusercategories(self, user):
        print(f"{bcolors.BOLD}Selecione uma categoria:{bcolors.ENDC}")
        from Controller import CategoryController
        categories = CategoryController.CategoryController().get_categories()
        for i in range(len(categories)):
            print(f"{i+1} - {categories[i]['name']}")
        print("0 - Carrinho de Compras")
        category = input("")

        try:
            category = int(category)
        except:
            main.showusercategories(self, user)
        if category == 0:
            print(f"\n{bcolors.BOLD}CARRINHO DE COMPRAS:{bcolors.ENDC}")
            if not cart:
                print("Você não possui nenhum item no carrinho!")
            for i in range(len(cart)):
                print(f"{bcolors.BOLD}ID: {bcolors.ENDC}{i}{bcolors.BOLD} - NOME:{bcolors.ENDC} {cart[i]['name']}{bcolors.BOLD} - VALOR: {bcolors.ENDC}R${cart[i]['price']}")
            input("Pressione qualquer tecla para continuar...")
            if cart:
                main.cartremovequestion(self, user)
            else:
                main.showusercategories(self, user)
        if not category >= 1 and not category <= len(categories):
            print(f"{bcolors.WARNING}Selecione um produto válido!{bcolors.ENDC}")
            main.showusercategories(self, user)
        category = categories[category - 1]["id"]
        main.showuserproducts(self, user, category)

    def showuserhome(self, user):
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
        print(("\t" * 14) + f"{bcolors.WARNING}WOW você é um cliente registrado, por conta disso os preços custam a metade do dobro!{bcolors.ENDC}")


        print(f'{bcolors.OKGREEN}Olá {user["name"]}, seja bem vindo!\n{bcolors.ENDC}')
        main.showusercategories(self, user)




