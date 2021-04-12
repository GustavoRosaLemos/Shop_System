class DatabaseController:
    def initdatabase(self):
        # Criar a tabela Users caso não exista
        try:
            users = open("Model/Users.txt", "r")
        except:
            users = open("Model/Users.txt", "x")
            with open("Model/Users.txt", "w") as file:
                file.write("[]")

        # Criar a tabela Products caso não exista
        try:
            products = open("Model/Products.txt", "r")
        except:
            products = open("Model/Products.txt", "x")
            with open("Model/Products.txt", "w") as file:
                file.write("[]")

        # Criar a tabela Category caso não exista
        try:
            categorys = open("Model/Category.txt", "r")
        except:
            categorys = open("Model/Category.txt", "x")
            with open("Model/Category.txt", "w") as file:
                file.write("[]")

        # Criar a tabela Cards caso não exista
        try:
            categorys = open("Model/Category.txt", "r")
        except:
            categorys = open("Model/Category.txt", "x")
            with open("Model/Category.txt", "w") as file:
                file.write("[]")

        # Criar a tabela History caso não exista
        try:
            history = open("Model/History.txt", "r")
        except:
            history = open("Model/History.txt", "x")
            with open("Model/History.txt", "w") as file:
                file.write("[]")