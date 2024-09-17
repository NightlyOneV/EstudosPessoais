import sqlite3
import sys

class New_SQL:
    
    def __init__(self):
        self.connection = None 
        self.Cursor = None
        self.startConnection()
    
    def startConnection(self):
        try:
            self.connection = sqlite3.connect("SQLusers.db")
            self.Cursor = self.connection.cursor()
            self.Cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (Nome TEXT, Email TEXT, Senha TEXT)")
            self.dbStartUp()
            
        except sqlite3.Error as Err:
            print(f"Ocorreu um erro inesperado: {Err}")
            sys.exit()
            
    def dbStartUp(self):
        print(f"Modificações totais da DB: {self.connection.total_changes}")
        
    def insertData(self, nome, email, senha):
        self.Cursor.execute(
            "INSERT INTO usuarios (Nome, Email, Senha) VALUES (?, ?, ?)",
            (nome,
            email,
            senha)
        )
        self.connection.commit()
        
    def returnExisting(self, key, value, profile):
        try:
            query = f"SELECT * FROM usuarios WHERE {key} = ?"
            self.Cursor.execute(query, (value,))
            result = self.Cursor.fetchone()
            
            if result is None:
                return True
            else:
                if profile == True: 
                    return [result]
                return False
            
        
        except sqlite3.Error as Err:
            print(f"Um erro inesperado ocorreu: {Err}")
            sys.Exit()
        
    def closeConnection(self):
        if self.connection:
            self.connection.close()
        