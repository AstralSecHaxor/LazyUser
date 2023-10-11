
import os
import shutil

# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" # vermelho 
bra = "\33[1;37m" # branco
am = '\033[33m' # Amarelo 

diretorio = "/usr/bin"

# Lista de diretórios a serem ignorados durante a cópia
diretorios_ignorados = [".git"]

def executavel():
    os.system(f"rm -rf {diretorio}/UserTool")
    os.system(f"cp -r {diretorio}/LazyUser/modules/UserTool {diretorio}")
    os.system(f"chmod +x {diretorio}/UserTool") 
    
    os.system(f"rm -rf {diretorio}/usertool")
    os.system(f"cp -r {diretorio}/LazyUser/modules/usertool {diretorio}")
    os.system(f"chmod +x {diretorio}/usertool") 
    os.system(f"cp -r .git {diretorio}/LazyUser")
    print(f"""
    {vlh}Uso:{bra}
  Para invocar a ferramenta, utilize um dos seguintes comandos:
  - {am}UserTool{bra}
  - {am}usertool{bra}
    """)

def LazyUser():
    # Pasta a ser criada
    pasta = "LazyUser"
    pasta_caminho = os.path.join(diretorio, pasta)
    
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

# Restante do seu código...

diretorio_termux = "/data/data/com.termux/files/usr/bin"

def executavel_termux():
    os.system(f"rm -rf {diretorio_termux}/UserTool")
    os.system(f"cp -r {diretorio_termux}/LazyUser/modules/UserTool {diretorio_termux}")
    os.system(f"chmod +x {diretorio_termux}/UserTool") 
    
    os.system(f"rm -rf {diretorio_termux}/usertool")
    os.system(f"cp -r {diretorio_termux}/LazyUser/modules/usertool {diretorio_termux}")
    os.system(f"chmod +x {diretorio_termux}/usertool") 
    print(f"""
{vlh}Uso:{bra}
      Para invocar a ferramenta, utilize um dos seguintes comandos:
      - {am}UserTool{bra}
      - {am}usertool{bra}
    """)

def termux_lazyuser():
    # Diretório a ser verificado
    
    # Pasta a ser criada
    pasta = "LazyUser"
    pasta_caminho = os.path.join(diretorio_termux, pasta)
    
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

def verificar_sistema():
    sistema = os.popen('uname -o').read().strip()
    if sistema == "Android":
        return termux_lazyuser()
    elif os.path.exists('/etc/os-release'):
        with open('/etc/os-release', 'r') as os_release_file:
            lines = os_release_file.readlines()
            for line in lines:
                if line.startswith('ID='):
                    distro_id = line.split('=')[1].strip().strip('"')
                    if distro_id.lower() == 'ubuntu':
                        return LazyUser()
                    elif distro_id.lower() == 'debian':
                        return LazyUser()
    return "Sistema não identificado"

sistema_atual = verificar_sistema()

