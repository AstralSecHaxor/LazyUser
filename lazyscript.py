import os
from time import sleep as timeout
#from modules.lazydb import *
from modules.funcoes import *
from modules.logos import *

vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" #vermelho 
bra = "\33[1;37m" # branco
az = '\033[34m' # Azul
ma = '\033[35m' #Magento
am = '\033[33m' #Amarelo 


banner_inicial()
while True:
    try:
        lazyscript = input(f"{vd}LazyUser ~$ {bra}")
        option_control  = lazyscript.replace(" ", "")
    except KeyboardInterrupt:
        sair_do_programar().exit()
    except EOFError:
        sair_do_programar().exit()
            
    
    # Category Coletar de informações
    if option_control == "1" or option_control == "01":
        coletainfox()
        
        
    ## Category análise de vulnerabilidades
    elif option_control == "2" or option_control == "02":
        analisevulnx()
        
    elif option_control == "3" or option_control == "03":
        pass
    
    
    elif option_control == "x" or option_control == "X": atualizar() # Opção de atualização do LazyScript
    elif option_control == "00" or option_control =="0": sair_do_programar()
    
    else:
        print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :({b}");timeout(1);
        banner_inicial()