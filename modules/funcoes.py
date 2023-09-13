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
        elif infox == "12": blackbox()
        elif infox == "13": xd3v()
        elif infox == "14": crips()
        elif infox == "15": sir()
        elif infox == "16": evilURL()
        elif infox == "17": striker()
        elif infox == "18": xshell()
        elif infox == "19": owscan()
        elif infox == "20": osif()
        elif infox == "21": devploit()
        elif infox == "22": namechk()
        elif infox == "23": auxile()
        elif infox == "24": inther()
        elif infox == "25": ginf()
        elif infox == "26": gpstr()
        elif infox == "27": asu()
        elif infox == "28": fim()
        elif infox == "29": maxsubdofinder()
        elif infox == "30": pwnedOrNot()
        elif infox == "31": maclook()
        elif infox == "32": billcypher()
        elif infox == "33": dnsrecon()
        elif infox == "34": zphisher()
        elif infox == "35": mrsip()
        elif infox == "36": sherlock()
        elif infox == "37": userrecon()
        elif infox == "38": phoneinfoga()
        elif infox == "39": sitebroker()
        elif infox == "40": maigret()
        elif infox == "41": gathetool()
        elif infox == "42": adbtk()
        elif infox == "43": tekdefense()
        elif infox == "44": eagleeye()
        elif infox == "45": eyewitness()
        elif infox == "46": inspy()
        elif infox == "47": leaked()
        elif infox == "48": fierce()
        elif infox == "49": gasmask()
	
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