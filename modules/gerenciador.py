#!/usr/bin/env python
#  _____________________________________________________
# +=[ Version 0.2 - beta                               
# +=[ BY: AstralSecHaxor From Brazil                   
# +=[ YouTube: https://youtube.com/@AstralSec_Haxor    
# +=[ Github: https://github.com/AstralSecHaxor/LazyUser
#  —————————————————————————————————————————————————————

# lazyuser.py USARÁ ESTE SCRIPT COMO SEU GERENCIADOR DE INSTALAÇÃO DAS FERRAMENTAS. 
# AQUI ESTARÃO TODAS AS FUNÇÕES DE INVOCAR AS FERRAMENTAS."

import os, sys, time
import urllib.request
from modules.logos import *
from time import sleep as timeout
## Importando as categoria
from modules.categories.web_hacks import *
from modules.categories.eng_reversa import *
from modules.categories.ataq_senhas import *
from modules.categories.ataq_sem_fio import *
from modules.categories.analise_vulns import *
from modules.categories.coletar_infos import *
from modules.categories.avali_databases import *
from subprocess import check_output as inputstream


# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vrd='\033[0;32m'   # Verde
vlh = "\33[1;31m" #vermelho 
bra = "\33[1;37m" # branco
az = "\033[34m" # Azul
ma = "\033[35m" #Magento
am = "\033[33m" #Amarelo 

##############################################################
    ## categoria Coletar de informações
def coletar_informacoes():
    try:
        banner_coletar_informacoes()
        coletarinfox = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/Coletar de Informações{az}]\n{vd}╰─>{vlh}$ {bra}") 
        remove_espaco = coletarinfox.replace(" ", "")
        if remove_espaco == "": 
            return banner_inicial()
                
        multi = [int(x) for x in remove_espaco.split(',')]
        for infox in multi:
            if infox == 0.1 or infox == 1: nmap()
            elif infox == 0.2 or infox == 2: red_hawk()
            elif infox == 0.3 or infox == 3: dtect()
            elif infox == 0.4 or infox == 4: sqlmap()
            elif infox == 0.5 or infox == 5: reconDog()
            elif infox == 0.6 or infox == 6: androZenmap()
            elif infox == 0.7 or infox == 7: sqlmate()
            elif infox == 0.8 or infox == 8: astraNmap()
            elif infox == 0.9 or infox == 9: mapeye()
            elif infox == 10: easyMap()
            elif infox == 11: crips()
            elif infox == 12: evilURL()
            elif infox == 13: striker()
            elif infox == 14: xshell()
            elif infox == 15: owscan()
            elif infox == 16: osif()
            elif infox == 17: namechk()
            elif infox == 18: auxile()
            elif infox == 19: inther()
            elif infox == 20: ginf()
            elif infox == 21: asu()
            elif infox == 22: fim()
            elif infox == 23: pwnedOrNot()
            elif infox == 24: dnsrecon()
            elif infox == 25: zphisher()
            elif infox == 26: mrsip()
            elif infox == 27: userrecon()
            elif infox == 28: phoneinfoga()
            elif infox == 29: sitebroker()
            elif infox == 30: gathetool()
            elif infox == 31: adbtk()
            elif infox == 32: tekdefense()
            elif infox == 33: eagleeye()
            elif infox == 34: eyewitness()
            elif infox == 35: inspy()
            elif infox == 36: fierce()
            elif infox == 37: gasmask()
            elif infox == 38: sherlock()
            
            elif infox == 00 or infox == 0: 
                sair_do_programar()
                
            else:
                print(f"{vlh}\nUps! {bra}'{remove_espaco}'{vlh} opção inválida :({vd}");timeout(1);
                return coletar_informacoes()
        backmenu() 
        lazy = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/Coletar de Informações{az}]\n{vd}╰─>{vlh}$ {bra}")  # input pós instalação 
        option_control  = lazy.replace(" ", "")
        if option_control == "00" or option_control == "0":
            exit()
        elif option_control == "":
            return coletar_informacoes()
        else:
            return coletar_informacoes()
            
            
    except ValueError:
        print(f"\n{vlh}Ups! {bra}'{coletarinfox}' {vlh}Insira apenas números");timeout(1)
        return coletar_informacoes()
    
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()
            
        return coletar_informacoes()

##############################################################
    ## Categoria análise de vulnerabilidades
def analise_vulnerabilidades():
    try:
        banner_analise_vulnevabilidade()
        analise_vuln = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/Análise Vulnerabilidades{az}]\n{vd}╰─>{vlh}$ {bra}") 
        remove_espaco = analise_vuln.replace(" ", "")
        if remove_espaco == "": 
            return banner_inicial()
                
        multi = [int(x) for x in remove_espaco.split(',')]
        for vulnx in multi:
            if  vulnx == 0.1 or vulnx == 1: sqliv()
            elif  vulnx == 0.2 or vulnx == 2: sqlscan()
            elif  vulnx == 0.3 or vulnx == 3: wordpreSScan()
            elif  vulnx == 0.4 or vulnx == 4: wpscan()
            elif  vulnx == 0.5 or vulnx == 5: wordpresscan()
            elif  vulnx == 0.6 or vulnx == 6: tmscanner()
            elif  vulnx == 0.7 or vulnx == 7: rang3r()
            elif  vulnx == 0.8 or vulnx == 8: routersploit()
            elif  vulnx == 0.9 or vulnx == 9: sh33ll()
            elif  vulnx == 10: xplsearch()
            elif  vulnx == 11: androbugs()
            elif  vulnx == 12: clickjacking()
            elif  vulnx == 13: sn1per()
            
            elif vulnx == 00 or vulnx == 0: 
                sair_do_programar()
                
            else:
                print(f"{vlh}\nUps! {bra}'{remove_espaco}'{vlh} opção inválida :({vd}");timeout(1);
                return analise_vulnerabilidades()
        backmenu() 
        lazy = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/Análise Vulnerabilidades{az}]\n{vd}╰─>{vlh}$ {bra}")  # input pós instalação 
        option_control  = lazy.replace(" ", "")
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return analise_vulnerabilidades()
        else:
            return analise_vulnerabilidades()
            
    except ValueError:
        print(f"\n{vlh}Ups! {bra}'{analise_vuln}' {vlh}Insira apenas números");timeout(1)
        return analise_vulnerabilidades()
    
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()
            
        return analise_vulnerabilidades()

##############################################################
  ## Categoria de web_hacking
def web_hacking():
    try:
        banner_web_hacking()
        web_hax = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/Web Hacking{az}]\n{vd}╰─>{vlh}$ {bra}") 
        remove_espaco = web_hax.replace(" ", "")
        if remove_espaco == "": 
            return banner_inicial()
                
        multi = [int(x) for x in remove_espaco.split(',')]
        for webhx in multi:
            if webhx == 0.1 or webhx == 1: webdav()
            elif webhx == 0.2 or webhx == 2: webmassploit()
            elif webhx == 0.3 or webhx == 3: atlas()
            elif webhx == 0.4 or webhx == 4: sqldump()
            elif webhx == 0.5 or webhx == 5: websploit()
            elif webhx == 0.6 or webhx == 6: xattacker()
            elif webhx == 0.7 or webhx == 7: xsstrike()
            elif webhx == 0.8 or webhx == 8: breacher()
            elif webhx == 0.9 or webhx == 9: kodork()
            elif webhx == 10: apsca()
            elif webhx == 11: fade()
            elif webhx == 12: xss_payload_list()
            elif webhx == 13: xadmin()
            elif webhx == 14: cmseek()
            elif webhx == 15: cmsmap()
            elif webhx == 16: crawlbox()
            elif webhx == 17: lfisuite()
            elif webhx == 18: parsero()
            elif webhx == 19: sublist3r()
            elif webhx == 20: wppluginscanner()
            elif webhx == 21: whatweb()
            elif webhx == 22: fuxploider()
            
            elif webhx == 00 or webhx == 0: 
                sair_do_programar()
                
            else:
                print(f"{vlh}\nUps! {bra}'{remove_espaco}'{vlh} opção inválida :({vd}");timeout(1);
                return web_hacking()
        backmenu() 
        lazy = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/Web Hacking{az}]\n{vd}╰─>{vlh}$ {bra}")  # input pós instalação 
        option_control  = lazy.replace(" ", "")
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return web_hacking()
        else:
            return web_hacking()
            
    except ValueError:
        print(f"\n{vlh}Ups! {bra}'{web_hax}' {vlh}Insira apenas números");timeout(1)
        return web_hacking()
    
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()
            
        return web_hacking()


##############################################################
  ## Categoria Avaliações de Banco de dados
def avaliacoes_de_banco_de_dados():
    try:
        banner_avali_banco_de_dados()
        avali_banco = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/Avaliações de banco de dados{az}]\n{vd}╰─>{vlh}$ {bra}") 
        remove_espaco = avali_banco.replace(" ", "")
        if remove_espaco == "": 
            return banner_inicial()
                
        multi = [int(x) for x in remove_espaco.split(',')]
        for avali_banco in multi:
            if avali_banco == 0.1 or avali_banco == 1: dbdat()
            elif avali_banco == 0.2 or avali_banco == 2: nosqlmap()
            elif avali_banco == 0.3 or avali_banco == 3: audit_couchdb()
            
            elif avali_banco == 00 or avali_banco == 0: 
                sair_do_programar()
                
            else:
                print(f"{vlh}\nUps! {bra}'{remove_espaco}'{vlh} opção inválida :({vd}");timeout(1);
                return avaliacoes_de_banco_de_dados()
        backmenu() 
        lazy = input(f"{vd}┬─{az}[{am}A.S.H{vlh}♘{bra}{sistema_atual}{az}]{vd}─{az}[{ma}~/Avaliações de banco de dados{az}]\n{vd}╰─>{vlh}$ {bra}")  # input pós instalação 
        option_control  = lazy.replace(" ", "")
        if option_control == "00" or option_control == "0":
            sair_do_programar()
        elif option_control == "":
            return avaliacoes_de_banco_de_dados()
        else:
            return avaliacoes_de_banco_de_dados()
            
    except ValueError:
        print(f"\n{vlh}Ups! {bra}'{avali_banco}' {vlh}Insira apenas números");timeout(1)
        return avaliacoes_de_banco_de_dados()
    
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()
            
        return avaliacoes_de_banco_de_dados()


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
            print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :( \n{bra}");timeout(2);
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
            print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :( \n{bra}");timeout(2);
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
