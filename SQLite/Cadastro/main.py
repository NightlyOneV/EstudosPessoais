from registroUsuario import Usuario
from bancoDados import New_SQL

def main():
    dataBase = New_SQL()
    novoUsuario = Usuario(dataBase)

if __name__ == "__main__":
    main()

