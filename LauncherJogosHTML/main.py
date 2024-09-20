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
        self.setWindowTitle("Launcher Teste")
        self.setGeometry(100,100,800,800)
        
        self.layout = QVBoxLayout(self)
        self.h_layout = QHBoxLayout(self)
        
        self.game_list = QListWidget()
        self.loadGameList()
        self.game_list.itemClicked.connect(self.loadGame)
        
        self.browser = QWebEngineView()
        
        self.h_layout.addWidget(self.game_list, 1)
        self.h_layout.addWidget(self.browser, 1)
        self.layout.addLayout(self.h_layout)

    def loadGameList(self):
        self.game_dir = 'jogos_html'
        print(f"Caminho absoluto: {os.path.abspath(self.game_dir)}")
        for folder in os.listdir(self.game_dir):
            folder_path = os.path.join(self.game_dir, folder)
            if os.path.isdir(folder_path) and 'index.html' in os.listdir(folder_path):
                self.game_list.addItem(folder)  

    def loadGame(self, item):
        game_folder = os.path.join(self.game_dir, item.text())
        game_html = os.path.join(game_folder, 'index.html')
        self.browser.setUrl(f'file:///{os.path.abspath(game_html)}')
        
        
        
main()