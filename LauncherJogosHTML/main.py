import sys 
import subprocess 

def main():
    pass

def PKG_install(pkg): # Função pra dar pip install em libs se necessário.
    print(f"Efetuando a instalação da lib: {pkg}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg]) 
  
def PKG_importSetup(): # Função para dar import nas libs.
    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QHBoxLayout
    from PySide6.QtWebEngineWidgets import QWebEngineView
    
def PKG_verify(): # Verificando se o usuário tem as libs, se não vamos botar para baixar.
    try: 
        PKG_importSetup()
    except ImportError:
        PKG_install("pyside6")
        PKG_importSetup()
    
    
