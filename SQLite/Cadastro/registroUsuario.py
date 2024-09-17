class Usuario:
    
    def Cadastro_InserirDados(self, key, value):
        if key == "Email" and self.dataBase.returnExisting("Email", value, False) != True:
            self.Cadastro_InserirDados("Email", input("Já existe um usuário com este Email, digite um Email válido: "))
    
        self.Info[key] = value
    
    def Login_InserirDados(self, key, value):
        if self.dataBase.returnExisting(key, value, False) == False:
            self.Info[key] = value
        else:
            self.Login_InserirDados(key, input("Invalido, digite novamente: "))
    
    def Retornar_Existente(self):
        return self.dataBase.returnExisting("Email", self.Info["Email"], True)
    
    def StartSignup(self):
        self.Cadastro_InserirDados("Nome", input("Digite seu nome de usuário: "))
        self.Cadastro_InserirDados("Email", input("Digite seu Email: "))
        self.Cadastro_InserirDados("Senha", input("Digite sua Senha: "))
        
        self.dataBase.insertData(self.Info["Nome"],
                                self.Info["Email"],
                                self.Info["Senha"])
    
    def StartLogin(self):
        self.Login_InserirDados("Email", input("Digite um Email existente: "))
        self.Login_InserirDados("Senha", input("Digite corretamente sua senha: "))
        self.User = self.Retornar_Existente()
    
    def __init__(self, Con, State):
            
        self.dataBase = Con
        self.Info = {
            "Nome": None,
            "Senha": None,
            "Email": None
        }
                    
        if State == 1:
            self.StartSignup()
        else:
            self.StartLogin()