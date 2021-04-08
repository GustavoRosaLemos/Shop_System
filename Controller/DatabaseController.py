class DatabaseController:
    def initdatabase(self):
        # Criar a tabela ids caso não exista
        try:
            ids = open("Model/Ids.txt", "r")
        except:
            ids = open("Model/Ids.txt", "x")

        # Criar a tabela Users caso não exista
        try:
            users = open("Model/Users.txt", "r")
        except:
            users = open("Model/Users.txt", "x")

        # Criar a tabela Products caso não exista
        try:
            products = open("Model/Products.txt", "r")
        except:
            products = open("Model/Products.txt", "x")

        # Criar a tabela Category caso não exista
        try:
            categorys = open("Model/Category.txt", "r")
        except:
            categorys = open("Model/Category.txt", "x")

        print("Banco de dados iniciado!")

