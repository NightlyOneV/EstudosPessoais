from registroUsuario import Usuario
from bancoDados import New_SQL

dataBase = New_SQL()
usuarioLogado = None

def iniciarAcao():
    acao = None 
    
    try:
        acao = int(input("Digite 1 para iniciar um cadastro\nDigite 2 para iniciar um login\nDigite:"))
    except:
        print("Inválido!")
        acao = int(input("Digite 1 para iniciar um cadastro\nDigite 2 para iniciar um login\nDigite:"))
        
    match acao:
        case 1:
            # Cadastro
            Usuario(dataBase, 1)

            return
            
        case 2:
            # Login
            usuarioLogado = Usuario(dataBase, 2)
            print(f"Bem vindo!\n{usuarioLogado.User}")
            return

def main():
    iniciarAcao()


if __name__ == "__main__":
    main()

