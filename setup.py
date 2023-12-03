#!/usr/bin/env python
#  _____________________________________________________
# +=[ Version 0.2 - beta                               
# +=[ BY: AstralSecHaxor From Brazil                   
# +=[ YouTube: https://youtube.com/@AstralSec_Haxor    
# +=[ Github: https://github.com/AstralSecHaxor/LazyUser
#  —————————————————————————————————————————————————————

import os
import shutil
from modules.logos import *

# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" # vermelho 
bra = "\33[1;37m" # branco
am = '\033[33m' # Amarelo 

# Lista de diretórios a serem ignorados durante a cópia
diretorios_ignorados = [".git"]

diretorio_bin = "/usr/bin"
diretorio_etc = "/etc"
def executavel():
    os.system(f"rm -rf {diretorio_bin}/LazyUser")
    os.system(f"cp -r {diretorio_etc}/LazyUser/modules/LazyUser {diretorio_bin}")
    os.system(f"chmod +x {diretorio_bin}/LazyUser") 
    
    os.system(f"rm -rf {diretorio_bin}/lazyuser")
    os.system(f"cp -r {diretorio_etc}/LazyUser/modules/lazyuser {diretorio_bin}")
    os.system(f"chmod +x {diretorio_bin}/lazyuser") 
    print(f"""
{vlh}Uso:{bra}
  Para invocar a ferramenta, utilize um dos seguintes comandos:
  - {am}LazyUser{bra}
  - {am}lazyuser{bra}
    """)

def LazyUser():
    # Pasta a ser criada
    pasta = "LazyUser"
    pasta_caminho = os.path.join(diretorio_etc, pasta)
    
    # Verifica se a pasta existe dentro do diretório
    if os.path.exists(pasta_caminho):
        # A pasta existe, então a excluímos
        shutil.rmtree(pasta_caminho)
    
    # Agora, criamos a pasta novamente
    os.mkdir(pasta_caminho)
    
    # Diretório raiz do script
    diretorio_origem = os.path.dirname(os.path.abspath(__file__))
    
    # Copia todos os arquivos e pastas da pasta de origem para LazyUser
    for item in os.listdir(diretorio_origem):
        origem = os.path.join(diretorio_origem, item)
        destino = os.path.join(pasta_caminho, item)
        
        if os.path.isdir(origem):
            # Se for uma pasta, copie-a recursivamente, ignorando diretórios específicos
            if item not in diretorios_ignorados:
                shutil.copytree(origem, destino)
            
        else:
            # Se for um arquivo, copie-o
            shutil.copy(origem, destino)
    executavel()


diretorio_termux_bin= "/data/data/com.termux/files/usr/bin"
diretorio_termux_etc = "/data/data/com.termux/files/usr/etc"
def executavel_termux():
    os.system(f"rm -rf {diretorio_termux_bin}/LazyUser")
    os.system(f"cp -r {diretorio_termux_etc}/LazyUser/modules/LazyUser {diretorio_termux_bin}")
    os.system(f"chmod +x {diretorio_termux_bin}/LazyUser") 
    
    os.system(f"rm -rf {diretorio_termux_bin}/lazyuser")
    os.system(f"cp -r {diretorio_termux_etc}/LazyUser/modules/lazyuser {diretorio_termux_bin}")
    os.system(f"chmod +x {diretorio_termux_bin}/lazyuser") 
    print(f"""
  {vlh}Uso:{bra}
  ----
      Para invocar a ferramenta, utilize um dos seguintes comandos:

      - {am}LazyUser{bra}
      - {am}lazyuser{bra}
""")

def termux_lazyuser():
    # Diretório a ser verificado
    
    # Pasta a ser criada
    pasta = "LazyUser"
    pasta_caminho = os.path.join(diretorio_termux_etc, pasta)
    
    # Verifica se a pasta existe dentro do diretório
    if os.path.exists(pasta_caminho):
        # A pasta existe, então a excluímos
        shutil.rmtree(pasta_caminho)
    
    # Agora, criamos a pasta novamente
    os.mkdir(pasta_caminho)
    
    # Diretório raiz do script
    diretorio_origem = os.path.dirname(os.path.abspath(__file__))
    
    # Copia todos os arquivos e pastas da pasta de origem para LazyUser
    for item in os.listdir(diretorio_origem):
        origem = os.path.join(diretorio_origem, item)
        destino = os.path.join(pasta_caminho, item)
        
        if os.path.isdir(origem):
            # Se for uma pasta, copie-a recursivamente, ignorando diretórios específicos
            if item not in diretorios_ignorados:
                shutil.copytree(origem, destino)
            
        else:
            # Se for um arquivo, copie-o
            shutil.copy(origem, destino)
    executavel_termux()

## Buscando sistema do usuário para executar block de código no logos.py
def obter_diretorio_base(sistema):
    if sistema == "Termux":
        return termux_lazyuser()
    elif sistema in ["Ubuntu", "Debian", "Kali"]:
        return LazyUser()
    else:
        return None
sistema_atual = verificar_sistema()
bIn = obter_diretorio_base(sistema_atual)
