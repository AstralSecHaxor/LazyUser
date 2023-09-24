"""
lazyuser.py USARÁ ESTE SCRIPT COMO SEU GERENCIADOR DE INSTALAÇÃO DAS FERRAMENTAS. 
AQUI ESTARÃO TODAS AS FUNÇÕES DE INVOCAR AS FERRAMENTAS."
"""
from time import sleep as timeout
import os, sys, time
import urllib.request
from subprocess import check_output as inputstream

## Importando as categoria do banco da dadas
from modules.logos import *
from modules.categories.analise_vulns import *
from modules.categories.coletar_infos import *
from modules.categories.web_hacks import *
from modules.categories.avali_databases import *
from modules.categories.ataq_senhas import *
from modules.categories.ataq_sem_fio import *


#variável com caminho até o diretório bin
Dirbin= "/data/data/com.termux/files/usr/bin"
#variável com caminho até o diretório home
CasaDir = "/data/data/com.termux/files/home"


##############################################################
    ## categoria Coletar de informações
def coletar_informacoes():
    try:
        banner_coletar_info()
        coletarinfox = input(f"{vd}LazyUser ~$ {bra}")
        infox = coletarinfox.replace(" ", "")
        if infox == "01" or infox == "1": nmap()
        elif infox == "02" or infox == "2": red_hawk()
        elif infox == "03" or infox == "3": dtect()
        elif infox == "04" or infox == "4": sqlmap()
        elif infox == "05" or infox == "5": infoga()
        elif infox == "06" or infox == "6": reconDog()
        elif infox == "07" or infox == "7": androZenmap()
        elif infox == "08" or infox == "8": sqlmate()
        elif infox == "09" or infox == "9": astraNmap()
        elif infox == "10": mapeye()
        elif infox == "11": easyMap()
        elif infox == "12": crips()
        elif infox == "13": evilURL()
        elif infox == "14": striker()
        elif infox == "15": xshell()
        elif infox == "16": owscan()
        elif infox == "17": osif()
        elif infox == "18": namechk()
        elif infox == "19": auxile()
        elif infox == "20": inther()
        elif infox == "21": ginf()
        elif infox == "22": gpstr()
        elif infox == "23": asu()
        elif infox == "24": fim()
        elif infox == "25": pwnedOrNot()
        elif infox == "26": dnsrecon()
        elif infox == "27": zphisher()
        elif infox == "28": mrsip()
        elif infox == "29": userrecon()
        elif infox == "30": phoneinfoga()
        elif infox == "31": sitebroker()
        elif infox == "32": gathetool()
        elif infox == "33": adbtk()
        elif infox == "34": tekdefense()
        elif infox == "35": eagleeye()
        elif infox == "36": eyewitness()
        elif infox == "37": inspy()
        elif infox == "38": fierce()
        elif infox == "39": gasmask()
	
        elif infox == "": 
            return banner_inicial()
            
        elif infox == "00" or infox =="0": 
            sair_do_programar()
            
        else:
            print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :( \n{b}");timeout(2);
            return coletar_informacoes()
            
        lazy = input(f"{vd}LazyUser ~$ {bra}") # input pós instalação 
        option_control  = lazy.replace(" ", "")
        
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return coletar_informacoes()
        
    except KeyboardInterrupt:
        sair_do_programar()
    except EOFError:
        sair_do_programar()
        
    return coletar_informacoes()


##############################################################
    ## Categoria análise de vulnerabilidades
def analise_vulnerabilidades():
    try:
        banner_analise_vulne()
        analise_vulne = input(f"{vd}LazyUser ~$ {bra}")
        vulnx = analise_vulne.replace(" ", "")
        if  vulnx == "01" or vulnx == "1": sqliv()
        elif  vulnx == "02" or vulnx == "2": sqlscan()
        elif  vulnx == "03" or vulnx == "3": wordpreSScan()
        elif  vulnx == "04" or vulnx == "4": wpscan()
        elif  vulnx == "05" or vulnx == "5": wordpresscan()
        elif  vulnx == "06" or vulnx == "6": tmscanner()
        elif  vulnx == "07" or vulnx == "7": rang3r()
        elif  vulnx == "08" or vulnx == "8": routersploit()
        elif  vulnx == "09" or vulnx == "9": sh33ll()
        elif  vulnx == "10": xplsearch()
        elif  vulnx == "11": androbugs()
        elif  vulnx == "12": clickjacking()
        elif  vulnx == "13": sn1per()
        
        elif vulnx == "": 
            return banner_inicial()
            
        elif vulnx == "00" or vulnx =="0": 
            sair_do_programar()
            
        else:
            print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :( \n{b}");timeout(2);
            return analise_vulnerabilidades()
            
        lazy = input(f"{vd}LazyUser ~$ {bra}") # input pós instalação 
        option_control  = lazy.replace(" ", "")
        
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return analise_vulnerabilidades()
        
    except KeyboardInterrupt:
        sair_do_programar()
    except EOFError:
        sair_do_programar()
    return analise_vulnerabilidades()


##############################################################
  ## Categoria de web_hacking
def web_hacking():
    try:
        banner_web_hacking()
        web_hacks = input(f"{vd}LazyUser ~$ {bra}")
        webhax = web_hacks.replace(" ", "")
        
        
        ## campo das funcoes
        if webhax == "01" or webhax == "1":
            pass
        
        
        elif webhax == "": 
            return banner_inicial()
            
        elif webhax == "00" or webhax =="0": 
            sair_do_programar()
            
        else:
            print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :( \n{b}");timeout(2);
            return web_hacking()
            
        lazy = input(f"{vd}LazyUser ~$ {bra}") # input pós instalação 
        option_control  = lazy.replace(" ", "")
        
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return web_hacking()
        
    except KeyboardInterrupt:
        sair_do_programar()
    except EOFError:
        sair_do_programar()
    return web_hacking()


##############################################################
  ## Categoria Avaliações de Banco de dados
def avaliacoes_databases():
    try:
        banner_avaliacoes_database()
        avali_database = input(f"{vd}LazyUser ~$ {bra}")
        databasex = avali_database.replace(" ", "")
        
        
        ## campo das funcoes
        if databasex == "01" or databasex == "1":
            pass
        
        
        elif databasex == "": 
            return banner_inicial()
            
        elif databasex == "00" or databasex =="0": 
            sair_do_programar()
            
        else:
            print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :( \n{b}");timeout(2);
            return avaliacoes_databases()
            
        lazy = input(f"{vd}LazyUser ~$ {bra}") # input pós instalação 
        option_control  = lazy.replace(" ", "")
        
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return avaliacoes_databases()
        
    except KeyboardInterrupt:
        sair_do_programar()
    except EOFError:
        sair_do_programar()
    return avaliacoes_databases()


##############################################################
  ## Categoria Ataques De Senhas
def ataque_senhas():
    try:
        banner_ataque_senhas()
        ataq_senhas = input(f"{vd}LazyUser ~$ {bra}")
        ataqqx = ataq_senhas.replace(" ", "")
        
        
        ## campo das funcoes
        if ataqqx == "01" or ataqqx== "1":
            pass
        
        
        elif ataqqx == "": 
            return banner_inicial()
            
        elif ataqqx == "00" or ataqqx =="0": 
            sair_do_programar()
            
        else:
            print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :( \n{b}");timeout(2);
            return ataque_senhas()
            
        lazy = input(f"{vd}LazyUser ~$ {bra}") # input pós instalação 
        option_control  = lazy.replace(" ", "")
        
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return ataque_senhas()
        
    except KeyboardInterrupt:
        sair_do_programar()
    except EOFError:
        sair_do_programar()
    return ataque_senhas()


##############################################################
  ## Categoria Ataques Sem 
def ataque_sem_fio():
    try:
        banner_ataque_sem_fio()
        ataq_sem_fio = input(f"{vd}LazyUser ~$ {bra}")
        ataqss = ataq_sem_fio.replace(" ", "")
        
        
        ## campo das funcoes
        if ataqss == "01" or ataqss == "1":
            pass
        
        
        elif ataqss == "": 
            return banner_inicial()
            
        elif ataqqx == "00" or ataqqx =="0": 
            sair_do_programar()
            
        else:
            print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :( \n{b}");timeout(2);
            return ataque_sem_fio()
            
        lazy = input(f"{vd}LazyUser ~$ {bra}") # input pós instalação 
        option_control  = lazy.replace(" ", "")
        
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return ataque_sem_fio()
        
    except KeyboardInterrupt:
        sair_do_programar()
    except EOFError:
        sair_do_programar()
    return ataque_sem_fio()
