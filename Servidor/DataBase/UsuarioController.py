from conexion import Data

class UsuarioController:
    def __init__(self):
        self.DataBase=Data()

    def select (self):
        self.lista=[]
        for row in self.DataBase.Selecionar("SELECT * FROM Usuario"):
            obj = {"ID":row[0],"PASSWORD":row[1],"NOMBRE":row[2],"FICHA":row[3]}
            self.lista.append(obj)
            return self.lista