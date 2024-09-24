import sys 
import subprocess 
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
def main():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        launcher = App()
        launcher.show()
        sys.exit(app.exec())
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LauncherHTML")
        self.setGeometry(100,100,800,800)
        
        self.layout = QVBoxLayout(self)
        self.h_layout = QHBoxLayout(self)
        
        self.game_list = QListWidget()
        self.loadGameList()
        self.game_list.itemClicked.connect(self.loadGame)
        
        self.browser = QWebEngineView()
        
        self.h_layout.addWidget(self.game_list, 0)
        self.h_layout.addWidget(self.browser, 1)
        self.layout.addLayout(self.h_layout)

    def loadGameList(self):
        self.game_dir = 'LauncherJogosHTML/jogos_html'
        abs_game_dir = os.path.abspath(self.game_dir)

        print(f"Caminho absoluto: {abs_game_dir}")

        if not os.path.exists(abs_game_dir):
            print("Não existe o diretório!")
            return

        for folder in os.listdir(abs_game_dir):
            print("Arquivo carregado!")
            folder_path = os.path.join(abs_game_dir, folder)
            
            if os.path.isdir(folder_path):
                files_in_folder = os.listdir(folder_path)
                if 'index.html' in files_in_folder:
                    self.game_list.addItem(folder)

    def loadGame(self, item):
        game_folder = os.path.join(self.game_dir, item.text())
        game_html = os.path.join(game_folder, 'index.html')
        
        game_path = os.path.abspath(game_html)
        file_url =  f"file:///{game_path.replace("\\","/")}"
        print(f"Loading game: {file_url}")
        self.browser.setUrl(file_url)
        
        
        
main()