import sqlite3
#from config import server
server='BsaeDePrueba.db'

class Data:
    def __init_(self):
        self.con = sqlite3.connect(server)
        self.cur = self.con.cursor()

    def Selecionar(self,query):
        table= self.cur.execute(query)
        self.con.close()
        return table

    def Modificar(self,query):
        self.cur.execute(query)
        self.con.commit()
        self.con.close()
        

