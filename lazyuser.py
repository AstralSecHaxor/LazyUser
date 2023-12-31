#!/usr/bin/env python
#  _____________________________________________________
# +=[ Version 0.2 - beta                               
# +=[ BY: AstralSecHaxor From Brazil                   
# +=[ YouTube: https://youtube.com/@AstralSec_Haxor    
# +=[ Github: https://github.com/AstralSecHaxor/LazyUser
#  —————————————————————————————————————————————————————

# ---------> AVISO <--------- #

#  O uso deste tool é estritamente de sua responsabilidade. 
#  Este tool foi desenvolvido para fins específicos e legais, como testes de segurança e conscientização. 
#  Qualquer uso indevido ou ilegal deste tool é expressamente proibido. 
#  O desenvolvedor deste tool não se responsabiliza por quaisquer consequências decorrentes do uso inadequado, ilegal ou antiético deste tool. 
#  Certifique-se de utilizar este tool de maneira ética e legal, respeitando todas as leis e regulamentos aplicáveis. 
#  Ao utilizar este tool, você concorda em fazê-lo de acordo com todas as leis e regulamentos vigentes em sua jurisdição.

# ---------> WARNING <--------- #

# The use of this tool is entirely your responsibility.
# This tool has been developed for specific and lawful purposes, such as security testing and awareness.
# Any misuse or illegal use of this tool is strictly prohibited.
# The developer of this tool does not assume responsibility for any consequences arising from the improper, illegal, or unethical use of this tool.
# Ensure that you use this tool ethically and legally, respecting all applicable laws and regulations.
# By using this tool, you agree to do so in accordance with all current laws and regulations in your jurisdiction.

# lib do bot: pip install python-telegram-bot
import os
from report_bug import *
from os.path import isdir
from modules.logos import *
from modules.gerenciador import *
from time import sleep as timeout

# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vrd='\033[0;32m'   # Verde
vlh = "\33[1;31m" #vermelho 
bra = "\33[1;37m" # branco
az = "\033[34m" # Azul
ma = "\033[35m" #Magento
am = "\033[33m" #Amarelo 

banner_inicial()
while True:
    try:
        lazyscript = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/{az}]\n{vd}╰─>{vlh}$ {bra}")
        option_control  = lazyscript.replace(" ", "")
        
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()
            
    ## Categoria: Coletar de informações
    if option_control == "1" or option_control == "01":
        coletar_informacoes()
        
    ## Categoria: análise de vulnerabilidades
    elif option_control == "2" or option_control == "02":
        analise_vulnerabilidades()
    
    ## Categoria: Web Hacking
    elif option_control == "3" or option_control == "03":
        web_hacking()
        
    ## Categoria: Avaliações de Banco de dados.
    elif option_control == "4" or option_control == "04":
        avaliacoes_de_banco_de_dados()
        
    # ## Categoria: Ataque Senhas
    # elif option_control == "5" or option_control == "05":
    #     ataque_senhas()
    
    # ## Categoria: ataques Sem Fio
    # elif option_control == "6" or option_control == "06":
    #     ataque_sem_fio()
        
    # elif option_control == "7" or option_control == "07":
    #     pass
    
    # elif option_control == "8" or option_control == "08":
    #     pass
    
    # elif option_control == "9" or option_control == "09":
    #     pass
    
    # elif option_control == "10":
    #     pass
    
    # elif option_control == "11":
    #     pass
    
    # elif option_control == "12":
    #     pass
    
    # elif option_control == "13":
    #     pass
    
    # elif option_control == "14":
    #     pass
    
    # elif option_control == "15":
    #     pass
    
    elif option_control == "16":
         ferramentas_engenharia_social()
    elif option_control == "x" or option_control == "X":
        reporte_relatorio()
    else:
        print(f"{vlh}\nUps! {bra}'{option_control}'{vlh} opção inválida :({vd}");timeout(1);
        banner_inicial()
