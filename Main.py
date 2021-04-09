<<<<<<< HEAD
from Controller.DatabaseController import *
from Controller.UserController import UserControl
db = DatabaseController()
db.initdatabase()
=======
import os
from Controller import DatabaseController
from Controller import HomeController

DatabaseController.DatabaseController().initdatabase() #Inicia o banco de dados
HomeController.main().initialize() #Inicia a parte visual





>>>>>>> 5732491b8cf69e8c45e602a0b24ff2e3b02c7529


