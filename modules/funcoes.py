from time import sleep as timeout
import os, sys, time
import urllib.request
from subprocess import check_output as inputstream
from modules.categories.analise_vulns import *
from modules.categories.coletar_infos import *
#from LazyScript.lazyscript import *
from modules.logos import *

Dirbin= "/data/data/com.termux/files/usr/bin"
#variável com caminho até o diretório home
CasaDir = "/data/data/com.termux/files/home"


    ## Category Coletar de informações
def coletainfox():
    try:
        coleinfox()
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
            return coletainfox()
            
        lazy = input(f"{vd}LazyUser ~$ {bra}") # input pós instalação 
        option_control  = lazy.replace(" ", "")
        
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return coletainfox()
        
    except KeyboardInterrupt:
        sair_do_programar().exit 
    return coletainfox()


    ## Category análise de vulnerabilidades
def analisevulnx():
    try:
        analisevuln()
        analisevulne = input(f"{vd}LazyUser ~$ {bra}")
        infox = analisevulne.replace(" ", "")
        if  analisevulne == "01" or analisevulne == "1": sqliv()
        elif  analisevulne == "02" or analisevulne == "2": sqlscan()
        elif  analisevulne == "03" or analisevulne == "3": wordpreSScan()
        elif  analisevulne == "04" or analisevulne == "4": wpscan()
        elif  analisevulne == "05" or analisevulne == "5": wordpresscan()
        elif  analisevulne == "06" or analisevulne == "6": tmscanner()
        elif  analisevulne == "07" or analisevulne == "7": rang3r()
        elif  analisevulne == "08" or analisevulne == "8": routersploit()
        elif  analisevulne == "09" or analisevulne == "9": sh33ll()
        elif  analisevulne == "10": xattacker()
        elif  analisevulne == "11": xplsearch()
        elif  analisevulne == "12": androbugs()
        elif  analisevulne == "13": clickjacking()
        elif  analisevulne == "14": sn1per()
        
        elif analisevulne == "": 
            return banner_inicial()
            
        elif analisevulne == "00" or infox =="0": 
            sair_do_programar()
            
        else:
            print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :( \n{b}");timeout(2);
            return analisevulnx()
            
        lazy = input(f"{vd}LazyUser ~$ {bra}") # input pós instalação 
        option_control  = lazy.replace(" ", "")
        
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return analisevulnx()
        
    except KeyboardInterrupt:
        sair_do_programar().exit 
    return analisevulnx()


## falhas no enter não volta quando da um erro