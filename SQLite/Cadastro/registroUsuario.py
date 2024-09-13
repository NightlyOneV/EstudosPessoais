class Usuario:
    
    def InserirDados(self, key, value):
        if key == "Email" and self.dataBase.returnExisting("Email", value) != True:
            self.InserirDados("Email", input("Já existe um usuário com este Email, digite um Email válido: "))
    
        self.Info[key] = value
    
    def __init__(self, Con):
            
        self.dataBase = Con
        
        self.Info = {
            "Nome": None,
            "Senha": None,
            "Email": None
        }
        
        self.InserirDados("Nome", input("Digite seu nome de usuário: "))
        self.InserirDados("Email", input("Digite seu Email: "))
        self.InserirDados("Senha", input("Digite sua Senha: "))
        
        self.dataBase.insertData(self.Info["Nome"],
                                 self.Info["Email"],
                                 self.Info["Senha"])