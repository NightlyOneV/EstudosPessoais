import random
import sqlite3
import customtkinter

class newApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pedra Papel Tesoura | O Jogo")
        self.geometry("800x600")
        self.resizable(False, False)

        self.MenuFrame = customtkinter.CTkFrame(self, width = 800, height=600, fg_color="white")
        self.GameFrame = customtkinter.CTkFrame(self, width = 800, height=600, fg_color="gray")

        #Menu
        self.GameTitle = customtkinter.CTkLabel(self.MenuFrame, width=400, height=100, text="Pedra vs Papel & Tesoura", font=("Arial", 30))
        self.PlayButton = customtkinter.CTkButton(self.MenuFrame, width=300, height=60, text="Play")
        self.GameCredits = customtkinter.CTkLabel(self.MenuFrame, width=100, height= 30, text="José Roberto Miranda")

        self.MenuFrame.pack(fill="both")
        self.PlayButton.grid(row=2,column=2)
        self.GameCredits.grid(row=3,column=1, pady=400, padx=30)
        self.GameTitle.grid(row=1, column=2)

        self.GameFrame.lower()

    def gameMenu(self):
        self.MenuFrame.lift()


class JogoNovo:
    def __init__(self):
        self._vitorias = 0
        self._derrotas = 0
        self._partidas = 0
        self._interromper = False
        self._escolha = ""
        self._escolha_inimiga = ""
        self.iniciar_partida()

    def verificar_situacao(self):
        e1 = self._escolha
        e2 = self._escolha_inimiga

        if e1 == e2:
            print("Empate! Próxima rodada.")
            return

        self._interromper = True

        if (e1 == "pedra" and e2 == "tesoura") or (e1 == "papel" and e2 == "pedra") or (e1 == "tesoura" and e2 == "papel"):
            print("Você ganhou!")
            self._vitorias += 1
        else:
            print("Você perdeu!")
            self._derrotas += 1

    def iniciar_partida(self):
        self._interromper = False
        self._escolha = ""
        self._escolha_inimiga = ""
        self._partidas += 1

        print(f"\nIniciando nova partida! Partida de número: {self._partidas}"
              f"\nVitórias: {self._vitorias}"
              f"\nDerrotas: {self._derrotas}"
              f"\nRate: {(self._vitorias + 1) / (self._derrotas + 1)}")
        while not self._interromper:
            self.escolha_usuario()
            self.escolha_inimiga()
            self.verificar_situacao()

        self.iniciar_partida()
    def escolha_usuario(self):
        while True:
            escolha = input("Qual sua jogada? Digite 'Pedra', 'Papel' ou 'Tesoura'\nDigite: ").lower()
            if escolha in ["pedra", "papel", "tesoura"]:
                self._escolha = escolha
                break
            else:
                print("Jogada inválida, tente novamente.")

    def escolha_inimiga(self):
        escolha = random.choice(["pedra", "papel", "tesoura"])
        print(f"Inimigo escolheu {escolha.capitalize()}!")
        self._escolha_inimiga = escolha


app = newApp()
app.mainloop()
'''
jogo = JogoNovo()
'''