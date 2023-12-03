#!/usr/bin/env python

#  _____________________________________________________
# +=[ Version 0.2 - beta                               
# +=[ BY: AstralSecHaxor From Brazil                   
# +=[ YouTube: https://youtube.com/@AstralSec_Haxor    
# +=[ Github: https://github.com/AstralSecHaxor/LazyUser
#  —————————————————————————————————————————————————————

# script responsável pela os gerenciamento dos banners

import subprocess
import os, sys, time
import urllib.request
import platform as mode
from time import sleep as timeout
from subprocess import check_output as inputstream

# Defina códigos de escape ANSI para cores
ci = "\33[1;36m" # Ciano
vlh = "\33[1;31m" # vermelho 
bra = "\33[1;37m" # branco
az = '\033[34m' # Azul
ma = '\033[35m' # Magento
am = '\033[93m'  # Amarelo Claro
verde= "\033[0;32m" # Verde
cinza = "\033[90m" # cinza

## Função de verificação do istema
def verificar_sistema():
    system_info = os.popen("uname -o").read().strip()
    if "Android" in system_info:
        return "Termux"
    elif os.path.exists('/etc/os-release'):
        with open('/etc/os-release', 'r') as os_release_file:
            lines = os_release_file.readlines()
            for line in lines:
                if line.startswith('ID='):
                    distro_id = line.split('=')[1].strip().strip('"')
                    if distro_id.lower() == 'ubuntu':
                        return "Ubuntu"
                    elif distro_id.lower() == 'debian':
                        return "Debian"
                    elif distro_id.lower() == 'kali':
                        return "Kali"
    return "LazyUser"
sistema_atual = verificar_sistema()

# Função para identificar ser sistema e linux
def identificar_sistema():
    sistema = mode.system()
    if sistema == "Linux":
        os.system("clear")
        return "Linux"
    else:
        print(f"{vlh}Ferramenta não projetada para esse sistema operacional{bra}")
        sys.exit()
# Função principal
def banner_inicial1():
    os.system("clear")
    print(f"""

{bra} /$$        /$$$$$$  /$$$$$$$$/$$     /$$
{bra}| $$       /$$__  $$|_____ $$|  $$   /$$/
{bra}| $$      | $$  \ $$     /$$/ \  $$ /$$/    {vlh}    /$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$
{bra}| $$      | $$$$$$$$    /$$/   \  $$$$/    {vlh}    | $$  | $$ /$$_____/ /$$__  $$ /$$__  $$
{bra}| $$      | $$__  $$   /$$/     \  $$/     {vlh}    | $$  | $$|  $$$$$$ | $$$$$$$$| $$  \__/
{bra}| $$      | $$  | $$  /$$/       | $$      {vlh}    | $$  | $$ \____  $$| $$_____/| $$
{bra}| $$$$$$$$| $$  | $$ /$$$$$$$$   | $$      {vlh}    |  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$
{bra}|________/|__/  |__/|________/   |__/      {vlh}     \______/ |_______/  \_______/|__/

╭──{az}[ {am}Copyright (c) 2023 {bra}By LazyUser {az}]{vlh}——{az}[ {am}V 0.2 {az}]{vlh}—{az}[ {am}CODED: {bra}ASTRALSEC{vlh}HAXOR {bra}FROM BRAZIL {az}]{vlh}──╮
╰╮                                                                                   {vlh}╭──╯
╭╯                                     {az}[ {verde}✔ {az}]{vlh}—{az}[{bra} Explore 51 Available Tools {az}]{vlh}──────────╯
╰╮
╭╯
╰┈➤ {az}[ {bra}Categories of Tools {az}]{bra}

    [ 01 ] Coletar de Informações             [ 09 ] Sniffing e Spoofing

    [ 02 ] Análise de Vulnerabilidades        [ 11 ] Ferramentas de Forenses

    [ 03 ] Web Hacking                        [ 12 ] Teste de Estresse

    [ 04 ] Avaliações de Banco de Dados       [ 13 ] Instalar Distribuições Linux

    [ 05 ] Ataques de Senhas                  [ 14 ] Utilitário Termux

    [ 06 ] Ataques Sem Fio                    [ 15 ] Análise de Malware

    [ 07 ] Engenharia Reversa                 [ 16 ] Ferramentas de Phishing

    [ 08 ] Ferramentas de Exploração


[ {vlh}CTRL+C {bra}] {vlh}Exit       {am}[ {bra}X {am}] {am}Reportar Problema

""")

def banner_inicial2():
    os.system("clear")
    print(f"""

{bra}██╗      █████╗ ███████╗██╗   ██╗    {vlh}  ██╗   ██╗███████╗███████╗██████╗
{bra}██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝    {vlh}  ██║   ██║██╔════╝██╔════╝██╔══██╗
{bra}██║     ███████║  ███╔╝  ╚████╔╝     {vlh}  ██║   ██║███████╗█████╗  ██████╔╝
{bra}██║     ██╔══██║ ███╔╝    ╚██╔╝      {vlh}  ██║   ██║╚════██║██╔══╝  ██╔══██╗
{bra}███████╗██║  ██║███████╗   ██║       {vlh}  ╚██████╔╝███████║███████╗██║  ██║
{bra}╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝       {vlh}   ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                                     {az} Version 0.2 - Beta⠀

                                        {az}[{verde} ✔ {az}]{bra} Explore 51 Available Tools

███ {am}CODED: {bra}AstralSec{vlh}Haxor {bra}From Brazil ██ {am}Copyright (c) 2023 {bra}By LazyUser ███


    {az}[ {bra}Categories of Tools {az}]{bra}

    [ 01 ] Coletar de Informações             [ 09 ] Sniffing e Spoofing
    
    [ 02 ] Análise de Vulnerabilidades        [ 11 ] Ferramentas de Forenses
    
    [ 03 ] Web Hacking                        [ 12 ] Teste de Estresse
    
    [ 04 ] Avaliações de Banco de Dados       [ 13 ] Instalar Distribuições Linux
    
    [ 05 ] Ataques de Senhas                  [ 14 ] Utilitário Termux
    
    [ 06 ] Ataques Sem Fio                    [ 15 ] Análise de Malware
    
    [ 07 ] Engenharia Reversa                 [ 16 ] Ferramentas de Phishing
    
    [ 08 ] Ferramentas de Exploração
    

[ {vlh}CTRL+C {bra}] {vlh}Exit       {am}[ {bra}X {am}] {am}Reportar Problema

""")

def banner_inicial():
    # Lista de funções de banners
    banners = [banner_inicial1, banner_inicial2]
    tempo_atual = int(time.time())
    indice_banner_aleatorio = tempo_atual % len(banners)
    resultado_banner = banners[indice_banner_aleatorio]()
    
    if resultado_banner is not None:
        return print(resultado_banner)
    else:
        pass

if __name__ == "__main__":
    banner_inicial()


def banner1(): ## banner de apresentação do menu de opções do tool
    os.system("clear")
    print(f"""
{ci} █{vlh}████
{ci}░░██{vlh}█
{ci} ░███ {vlh}        ██████    █████████ █████ ████
{ci} ░███   {vlh}     ░░░░░███  ░█░░░░███ ░░███ ░███
{ci} ░███       {vlh}  ███████  ░   ███░   ░███ ░███
{ci} ░███      █ █{vlh}██░░███    ███░   █ ░███ ░███
{ci} ███████████░░██{vlh}██████  █████████ ░░███████
{ci}░░░░░░░░░░░  ░░░░░{vlh}░░░  ░░░░░░░░░   ░░░░░███
{ci}                    {vlh}     ░░░░░     ███ ░███
{ci}                      {vlh}   ░         ░░██████   
{vlh}                                   ░░░░░  
{ci}            ███    █▄     {vlh}▄████████░░░████████    ▄████████ 
{ci}            ███    ███   ███{vlh}    ███░░ ███    ███   ███    ███ 
{ci}            ███    ███   ███   {vlh} █▀ ░  ███    █▀    ███    ███ 
{ci}            ███    ███   ███      {vlh}   ▄███▄▄▄      ▄███▄▄▄▄██▀ 
{ci}            ███    ███ ▀███████████ {vlh}▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
{ci}            ███    ███          ███   █{vlh}██    █▄  ▀███████████ 
{ci}            ███    ███    ▄█    ███   ███ {vlh}   ███   ███    ███ 
{ci}            ████████▀   ▄████████▀    ████████{vlh}██   ███    ███ 
   {ci}-----{vlh}> {am}Escolha sua ferramenta favorita.{vlh} <{ci}-----  {ci}█{vlh}██    ███
{bra}                                                   {ci}███{vlh}{bra}    {vlh}███{bra}
{vlh}┏━━━{bra}[ {vlh}Requer Privilégio #Root{bra} ]{vlh}                    {ci}███  {vlh}  ███{bra}""")

def banner2():
    os.system("clear")
    print(f"""{bra}
                                {az}           ⠀⠀⢀⣀⣤⣄⣀⡀⠀⠀⣀⣠⠤⠤⠤⠤⢤⣄⡀⠀⠀⠀⢀⣠⣤⣄⡀⠀
                                {az}           ⠀⡞⠉⠀⠀ ⠀⠉⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⢢⠴⠚⠉⠀ ⠀⠀⠙⡆
                                {az}             ⠘⡄                       ⣰⠷
{ci}⠀⠀⠀⠀⠀⠀⠀⠀⢶⠶⣶⡞⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀{az}⠀⠀⠀⠀⠀ ⠀⠀⠀⠀ ⠀⠀⠀⠀     ⢰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣏⠀
{ci}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠘⠟⢛⣿⠏⠀⠀⠀⠀{az}⠀ ⠀⠀⠀⠀⠀⠀⠀⠀          ⡟   {bra} BY: AstralSec{vlh}Haxor   {az}⠘⡆
{ci}⠀⠀ ⠀⠀⠀⠀⠀⠀⠸⠿⠟⠛⠃⠀⠀⢠⣾⠏⣀⡀    {az}                   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇
{ci}⠀⠀⢠⣤⣴⣶⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠻⠛⠛⠛⠃   {az}                    ⢻⡀⠀{bra}  Version 0.2 - Beta{az}⠀⠀⢀⣼⠏
{ci}⠀⠀⠈⠉⠉⣾⡿⠁                    {az}                ⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀
{ci}⠀⠀⠀⠀⣼⣿⣁⣀⣀⠀⠀⠀⢻⡟              {az}                ⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠀
{ci}⠀⠀⠀⠰⣿⠿⠿⠛⠛⠀⠀⠀⠛⠛⠃{bra}        ⠀  ⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀{az}⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⣀⣠⡤⢦⣀⣀⣀⣤⡴⠀⢀⡴⠳⠦⣄⣀⣠⡼⠟⠓⠶⠶⠞⠛⠀
{bra}     ⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣶⣿⠟⢿⡇⠀⠀⠀⠀⠀{az}⠀⠀⠀⠀⠀⠀    ⠀⠀⣠⠏⣠⠶⠛
{bra}⠀⠀⠀⠀⠀          ⠀⢀⣤⡶⠞⠛⠉⠉⠁⠀⠀⠈⠉⠉⠁⠀⠀⠀⣠⣿⡶⠾⢿⣿⠆⠀⠀{az}⠀⠀      ⠀⢀⣞⡵⠞⠉
{bra}⠀         ⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⢠⣺⡏⠀⠀⠀⠀{az}⠀ ⠀⠀⠀⠀⢀⣴⠟⠉
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⢀⡀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡝⢷⣄⠀⠀{az}⠀⠀   ⢀⣴⠟⠉
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⢀⡴⠚⠉⠀⠀⠀⠀⠀⠉⠒⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢪⡻⣦⠀⠀ {az}  ⠀⠎
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⣴⣋⡀⠤⠤⠤⢀⣀⠀⠀⠀⠀⠀⠑⡄⠀⠀⠀⠒⠒⠲⠤⣀⠀⠀⠀⠱⡽⣷⠀
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⣰⠋⠁⠀⠀⠀⠀⠀⠈⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⢱⡹⣇⠀
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⡏⠀⠀⠀⠘⣷⣤⣀⣀⡀⠈⡇⠀⠀⠀⠀⠀⠀⣀⠠⠤⠤⢀⣀⠀⠀⠱⡄⠀⢳⣿⡄
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⡄⠀⡇⠀⠀⠀⠀⠀⠉⠛⠋⠁⣰⢣⣶⣶⣤⣄⢀⡞⠁⠀⠀⠀⠀⠈⠙⠦⣀⢳⠀⠈⢿⡇
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠹⡄⢳⡀⠀⣀⡤⠤⠤⠄⠒⠊⠁⠈⢻⣿⠿⠟⢸⡀⠐⢷⣦⣤⣤⣤⠀⠀⠙⣾⠀⠀⢸⡇
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡘⢄⢻⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⠁⠀⠈⠳⣄⡀⠈⠉⠉⠀⠀⠀⢀⡏⠀⠀⣿⠃
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠑⠿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⡀⠀⠀⠀⢀⡜⠀⠀⢠⡿⠀
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⡈⠙⠳⢠⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⡠⠊⠀⢀⣠⣾⠁⠀
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠿⡟⠷⣤⣄⡀⠉⠉⠒⠢⡤⠤⣄⣀⣀⣀⠀⢀⡠⠤⠘⠋⠀⠤⢒⣽⠟⠁⠀⠀
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠈⠑⠦⣍⡁⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⣀⣤⣤⠶⠛⠁⠀⠀⠀⠀
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⡾⠀⠀⠀⠀⢠⠈⠉⠀⠀⠀⠀⠀⠀⠈⠉⠛⣿⡟⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
{bra}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⣸⡇⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿ {ci}-----{vlh}> {am}Escolha sua ferramenta favorita.{vlh} <{ci}-----
{bra}⠀⠀⠀⠀⠀⢀⣶⣶⣦⣼⠏⢠⡿⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡆       --------------------------------
{bra}⠀⠀⠀⠀⠀⢸⣇⡈⢉⡿⠀⣼⡇⠀⠀⠀⠀⣘⣿⠀⠀⢀⣤⣦⣄⠀⠀⠀⠀⠀⠈⣿⣷⣶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
{bra}⠀⠀⠀⠀⠀⠀⢿⣏⢺⣧⣾⠇⠀⠀⠀⠀⠀⣿⡟⠛⢻⡿⣿⢹⣿⡄⠀⠀⠀⠀⠀⢸⣿⣇⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
{bra}⠀⠀⠀⠀⠀⠀⣀⣽⠿⡿⠁⠀⠀⠀⠀⠀⡼⣿⠃⢀⣿⠟⢛⣟⢿⣷⠀⠀⠀⠀⠀⣸⣿⢯⣻⣿⣿⣦⡀⠀⠀⠀⠀⠀
{bra}⠀⠀⠀⢀⣰⣾⣿⣤⡘⠀⠀⠀⠀⠀⢀⠜⣼⠇⠀⣸⡏⢣⠿⢿⡹⣿⡀⠀⠀⠀⢰⡿⡟⠻⡿⣿⠄⠈⢿⣷⣄⠀⠀⠀
{bra}⢀⡀⣰⣿⡿⠋⣠⣼⠿⣧⡀⠀⠤⠚⢁⣼⠏⠀⠒⠻⠙⢼⡀⣸⢧⡿⠈⠑⢀⣴⠟⠳⠧⠴⣿⡟⠀⢀⣼⣏⣻⡆⠀⠀
{bra}⠧⢀⡻⣿⣤⣾⣏⣀⣀⣜⣿⣤⡴⠾⠿⣧⣤⣄⣀⣀⣀⣀⣨⣴⣿⡥⠶⠾⠿⠷⠶⠶⠶⠿⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀
{bra}⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠠⠄⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
{vlh}┏━━━{bra}[ {vlh}Requer Privilégio #Root{bra} ]{vlh} """)

def banner3():
    os.system("clear")
    print(f"""{ci}

                                      ⠀⠀⠀⠀⠀⠀⠀⠀⢶⠶⣶⡞⠀⠀⠀⢀⣀⣀⣀
                                         ⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠘⠟⢛⣿⠏
⠀⠀                                     ⠀⠀⠀⠀⠀⠀⠀⠸⠿⠟⠛⠃⠀⠀⢠⣾⠏⣀⡀
                                     ⠀⠀⢠⣤⣴⣶⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠻⠛⠛⠛⠃
⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀{ci}⠀⠀⠀⠈⠉⠉⣾⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{bra}⢀⣤⠤⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{ci}⠀⠀⠀⠀⠀⣼⣿⣁⣀⣀⠀⠀⠀⢻⡟{bra}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠒⠚⠛⠒⠀⠀⠙⠒⠒⠒⠒⠒⠤⢄⡀{ci}⠀ ⠀⠀⠀⠰⣿⠿⠿⠛⠛⠀⠀⠀⠛⠛⠃{bra}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⣟⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠑⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⠀⢀⣀⣤⠴⠖⡚⠋⠉⢩⣉⢉⠙⡒⠲⠤⣄⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⣄⠀⠈⢻⡉⡀⠀⠀⠈⠋⠁⠀⠀⠀⠈⠉⠑⠒⠀⠒⢮⡑⠢⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣟⠏⠀⢀⡤⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⢤⣀⣈⠢⠀⠀⢯⠁⣀⡤⠔⠂⠀⠀⠀⠀⠀⠀⠦⠤⣀⠀⠀⠈⠓⢬⡳⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⡘⠀⡴⠃⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⢁⠀⠀⠀⢠⠈⢹⡀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⢄⡁⠘⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡇⢠⢁⣠⠖⠋⠉⠀⠉⠑⡄⠀⠀⠀⠀⠀⢸⡀⠈⢦⣀⣠⠾⠀⠈⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡏⠃⠀⡏⠀⢆⠀⠀⢀⡧⠀⣽⠀⠀⠀⡀⠀⠀⠙⠦⢤⣀⣀⣀⣀⣠⡇⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀
⠀⠀⠀⠀⣀⣀⣀⣤⢴⣒⠿⠭⢳⠀⠀⢱⡀⠈⠓⠒⠛⣠⠜⠁⠀⠰⣿⣿⡿⠂⢠⠀⠀⠀⠀⠀⠀⣰⠃⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇
⠀⠀⠀⢸⣽⠉⠛⠊⠉⠀⠀⠀⠈⢧⠀⠀⠣⠤⠤⠒⠋⠁⠀⠀⠦⣀⡼⠟⠓⠒⠛⠀⠀⠀⠀⠀⡰⠃⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢻⡀
⠀⠀⠀⠀⣿⠀⡗⠢⣄⡀⠀⠀⠀⠈⢳⡀⠀⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⣠⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣾⡀
⠀⠀⠀⠀⢾⡀⢷⡼⠁⢈⡕⢦⣀⠀⠀⠙⠢⣄⠈⠑⠢⠄⠀⠀⠀⠀⠀⠀⠀⠀⠄⠒⠉⣠⠴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡄⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠗⡯⣥⣒⣦
⠀⠀⠀⠀⣈⣷⡜⣆⢀⡎⠀⠀⠈⢻⣤⡀⠀⠀⠉⠓⣢⡤⠤⣄⣀⣀⣀⣤⢤⡤⠖⠚⠉⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣳⡀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⡗⠚⠛⢻⡇
⠀⠀⢠⣾⡿⠿⣿⢾⡿⣀⠀⠀⡰⠃⠈⢳⡀⠀⠀⠀⠀⠉⠳⡄⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⣧⠀⢳⣀⣀⣀⣀⣀⣀⣀⣀⡠⠤⠴⣒⡛⢛⢳⠀⠀⠀⠀⠀⠀⠀⠃⠀⡀⣧⠀⠀⡜⢻
⠀⠀⣿⣻⡇⠀⠈⠻⣟⡪⣓⠦⣇⡀⢠⠏⢹⣄⠀⠀⠀⡀⠰⠁⠀⢀⣀⣤⠴⠖⠻⡄⠀⠀⠀⠀⠀⣿⢲⢸⠄⠀⠀⠀⢤⣶⣶⣊⣉⣉⣀⣀⠀⠀⠳⣇⠃⠀⠀⠀⠀⠀⡀⠐⡇⣿⡠⠊⠀⢸⡆
⠀⠀⣿⣻⠉⠉⠉⢉⣽⣿⣧⣍⣒⠪⠍⠉⠭⠭⢀⠀⠀⣸⣶⠛⠉⠉⠀⠐⠒⠒⠨⡇⠀⠀⠀⠀⠀⠀⠀⣾⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⢉⣽⠴⠀⠀⠀⠀⠀⡇⠀⡇⡟⠀⠀⢠⡏⠁
⢀⣔⠛⠭⠽⣯⣽⣿⡿⠚⠋⠉⠉⠉⠓⠒⠒⠒⠛⢻⣖⠟⠙⠓⠒⢲⠤⠤⣤⣀⣀⡇⠀⠀⠀⠀⠀⣀⠀⠁⡇⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⠸⡇⡀⠀⠀⠀⠘⠃⢸⢩⣇⣠⠴⠋
⠈⠉⠉⣳⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⡄⠀⠀⠀⢼⠉⢀⣿⠀⠀⣇⡇⠀⠀⠀⠀⣿⠀⠀⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⡤⠤⠤⢤⢤⡴⡇⡆⠀⠀⠀⠀⠀⠀⣸⠇
⠀⠀⣾⠘⣹⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠃⠀⠀⠀⠀⢀⣾⣿⠀⠀⣾⠁⠀⠀⠀⠀⠻⠀⣄⡇⠀⠀⠀⠀⠀⠀⠸⣎⠂⠀⠀⠀⢿⡞⠃⣿⠁⠀⠀⠀⢰⡇⢠⠇ Version 0.2 - Beta⠀
{verde} *{bra}⢹⡎⠁{verde}**************************{bra}⠸⡴⠀⠀⠀⠀⠀⠀⣿⡇{verde}***************{bra}⢹⣆⠀⠀⠀⠘⣡⡏{verde}**********************
⠀**  {am}Author:{bra} AstralSec{vlh}Haxor {bra}⠀  ⠈⢷⡀⠀⠀⠀⠀⢀⣿{ci}--{vlh}>{am} Escolha Sua F{bra}⠸⣎⢷⡒⣶⣯⡟{am}nta Favorita. {vlh}<{ci}-----{verde}**
 *******************************{bra}⠈⡟⢦⡤⢤⣴⣿⠃{verde}*****************{bra}⠈⠈⠻⠁⠋⠁{verde}***********************
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{bra}⠀⠈⠛⠸⣾⠙⠛⠀⠀⠀⠀ ⠀⠙⠋⢧⡟⠻⠏

{vlh}┏━━{bra}[ {vlh}Requer Privilégio #Root{bra} ]{vlh}""")

def banner():
    # Lista de funções de banners
    banners = [banner1, banner2, banner3]
    tempo_atual = int(time.time())
    indice_banner_aleatorio = tempo_atual % len(banners)
    resultado_banner = banners[indice_banner_aleatorio]()
    
    if resultado_banner is not None:
        return print(resultado_banner)
    else:
        pass

    ## banner de instalação das ferramentas.
def install_banner():
    os.system("clear")
    print(f"""{ma}
.------------------------------------------------------------------------.
 )                                                                      (
(    {ci}       ___           _        _                 _           {ma}        )
 )   {ci}      |_ _|_ __  ___| |_ __ _| | __ _ _ __   __| | ___      {ma}       (
(    {ci}       | || '_ \/ __| __/ _` | |/ _` | '_ \ / _` |/ _ \     {ma}        )
 )   {ci}       | || | | \__ \ || (_| | | (_| | | | | (_| | (_) |    {ma}       (
(    {ci}      |___|_| |_|___/\__\__,_|_|\__,_|_| |_|\__,_|\___/ ••• {ma}        )
 )   {ci}                                                            {ma}       (
'------------------------------------------------------------------------'""")

    ## banner de verificação ser a ferramenta já existente em algum diretório.
def Installed_banner(): 
    os.system("clear")
    print(f"""{ci}
.___________________________________________________________________________.
 )_{vlh}oooo{ci}_________________{vlh}oo{ci}____________{vlh}ooo{ci}________________{vlh}oo{ci}____________{vlh}oo{ci}__(
(___{vlh}oo{ci}__{vlh}oo{ci}_{vlh}ooo{ci}___{vlh}oooo{ci}___{vlh}oo{ci}_____{vlh}ooooo{ci}___{vlh}oo{ci}____{vlh}ooooo{ci}___{vlh}oooooo{ci}__{vlh}ooooo{ci}_____{vlh}oo{ci}___)
 )__{vlh}oo{ci}__{vlh}ooo{ci}___{vlh}o{ci}_{vlh}oo{ci}___{vlh}o{ci}_{vlh}oooo{ci}___{vlh}oo{ci}___{vlh}oo{ci}__{vlh}oo{ci}___{vlh}oo{ci}___{vlh}oo{ci}_{vlh}oo{ci}___{vlh}oo{ci}_{vlh}oo{ci}___{vlh}oo{ci}____{vlh}oo{ci}__(
(___{vlh}oo{ci}__{vlh}oo{ci}____{vlh}o{ci}___{vlh}oo{ci}____{vlh}oo{ci}____{vlh}oo{ci}___{vlh}oo{ci}__{vlh}oo{ci}___{vlh}oo{ci}___{vlh}oo{ci}_{vlh}oo{ci}___{vlh}oo{ci}_{vlh}oo{ci}___{vlh}oo{ci}____{vlh}oo{ci}___)
 )__{vlh}oo{ci}__{vlh}oo{ci}____{vlh}o{ci}_{vlh}o{ci}___{vlh}oo{ci}__{vlh}oo{ci}__{vlh}o{ci}_{vlh}oo{ci}___{vlh}oo{ci}__{vlh}oo{ci}___{vlh}oo{ci}___{vlh}oo{ci}_{vlh}oo{ci}___{vlh}oo{ci}_{vlh}oo{ci}___{vlh}oo{ci}________(
(__{vlh}oooo{ci}_{vlh}oo{ci}____{vlh}o{ci}__{vlh}oooo{ci}____{vlh}ooo{ci}___{vlh}oooo{ci}_{vlh}o{ci}_{vlh}ooooo{ci}__{vlh}oooo{ci}_{vlh}o{ci}__{vlh}oooooo{ci}__{vlh}ooooo{ci}_____{vlh}oo{ci}___)
 )_____________________________________________________________________{vlh}oo{ci}__(
(___________________________________________________________________________)
""")


def backmenu(): ## menu de opções para voltar ao menu  anterior ou sair 
    print(f"""
    {bra}[ {vlh}CTRL+C {bra}] ~> {vlh}Exit
    {bra}[ {vlh}enter {bra}] ~> {ci}Voltar ao menu anterior.
 """)
 
def backmenu_inicial(): ## menu de opções para voltar ao menu inicial ou sair
    print(f"""{bra}
   {bra}[ {vlh}CTRL+C {bra}] ~> {vlh}Exit{bra}
   [ {vlh}enter {bra}] ~> {ci}Voltar ao menu Inicial.{bra}
   [ {vlh}multi install{bra} ] ~> {ci}Faça uma sequência de opções separadas por vírgulas.
      {am}Ex{bra}: 3,23,6,19
""")

# coletar informacoes
def banner_coletar_informacoes():
    banner()
    print(f"""{vlh}┃
{vlh}┃
{vlh}┃{bra}[ 01 ] Nmap: Utilitário para descoberta de rede e auditoria de segurança.
{vlh}┃{bra}[ 02 ] Red Hawk: Coleta de informações, verificação de vulnerabilidades e rastreamento.
{vlh}┃{bra}[ 03 ] D-TECT: Ferramenta multifuncional para testes de penetração.
{vlh}┃{bra}[ 04 ] sqlmap: Ferramenta automática de injeção SQL e controle de banco de dados.
{vlh}┃{bra}[ 05 ] ReconDog: Ferramenta de coleta de informações e verificação de vulnerabilidades.
{vlh}┃{bra}[ 06 ] AndroZenmap: ?
{vlh}┃{bra}[ 07 ] sqlmate: Um amigo do SQLmap que fará o que você sempre esperou do SQLmap.
{vlh}┃{bra}[ 08 ] AstraNmap: Verificador de segurança usado para localizar hosts e serviços em uma rede de computadores.
{vlh}┃{bra}[ 09 ] MapEye: Rastreador de localização GPS preciso Android, IOS, Windows phones.
{vlh}┃{bra}[ 10 ] Easymap: Atalho do Nmap.
{vlh}┃{bra}[ 11 ] Crips: Esta ferramenta é uma coleção de ferramentas IP on-line que podem ser usadas para obter rapidamente informações sobre endereços IP, páginas da Web e registros DNS.
{vlh}┃{bra}[ 12 ] EvilURL: Gere domínios malignos unicode para ataque homógrafo de IDN e detecte-os.
{vlh}┃{bra}[ 13 ] Striker: Conjunto de verificação de reconhecimento e vulnerabilidade.
{vlh}┃{bra}[ 14 ] Xshell: Conjunto de ferramentas (ToolKit).
{vlh}┃{bra}[ 15 ] OWScan: Verificador da Web OVID.
{vlh}┃{bra}[ 16 ] OSIF: Informações de código aberto Facebook.
{vlh}┃{bra}[ 17 ] Namechk: Ferramenta OSINT baseada em namechk.com para verificar nomes de usuários em mais de 100 sites, fóruns e redes sociais.
{vlh}┃{bra}[ 18 ] AUXILE: Estrutura de análise de aplicativos da Web.
{vlh}┃{bra}[ 19 ] inther: Coleta de informações usando shodan, censys e hackertarget.
{vlh}┃{bra}[ 20 ] GINF: Ferramenta de coleta de informações do GitHub.
{vlh}┃{bra}[ 21 ] ASU: Kit de ferramentas para hackear o Facebook.
{vlh}┃{bra}[ 22 ] Fim: Downloader de imagens do Facebook.
{vlh}┃{bra}[ 23 ] PwnedOrNot: Ferramenta OSINT para encontrar senhas de contas de e-mail comprometidas.
{vlh}┃{bra}[ 24 ] DNSRecon: Avaliação de segurança e solução de problemas de rede.
{vlh}┃{bra}[ 25 ] Zphisher: Ferramenta automatizada de phishing.
{vlh}┃{bra}[ 26 ] Mr.SIP: Ferramenta de auditoria e ataque baseada em SIP.
{vlh}┃{bra}[ 27 ] UserRecon: Encontre nomes de usuário em mais de 75 redes sociais.
{vlh}┃{bra}[ 28 ] PhoneInfoga: Uma das ferramentas mais avançadas para escanear números de telefone usando apenas recursos gratuitos.
{vlh}┃{bra}[ 29 ] SiteBroker: Um utilitário multiplataforma baseado em python para coleta de informações e automação de testes de penetração.
{vlh}┃{bra}[ 30 ] GatheTOOL: Coleta de informações - API hackertarget.com
{vlh}┃{bra}[ 31 ] ADB-ToolKit: ?
{vlh}┃{bra}[ 32 ] TekDefense-Automater: Automater - URL IP e análise MD5 OSINT.
{vlh}┃{bra}[ 33 ] EagleEye: Persiga seus amigos. Encontre seus perfis do Instagram, FB e Twitter usando reconhecimento de imagens e pesquisa reversa de imagens.
{vlh}┃{bra}[ 34 ] EyeWitness: EyeWitness foi projetado para fazer capturas de tela de sites, fornecer algumas informações de cabeçalho do servidor e identificar credenciais padrão, se possível.
{vlh}┃{bra}[ 35 ] InSpy: Uma ferramenta de enumeração do LinkedIn baseada em python.
{vlh}┃{bra}[ 36 ] Fierce: Uma ferramenta de reconhecimento de DNS para localizar espaço IP não contíguo.
{vlh}┃{bra}[ 37 ] Gasmask: Ferramenta de coleta de informações - OSINT.
{vlh}┃{bra}[ 38 ] SherLock: Sherlock é uma ferramenta de código aberto que ajuda a rastrear perfis de mídia social e presença online de indivíduos, facilitando a coleta de informações públicas.
{vlh}┗[?]{bra}
""")
    backmenu_inicial()
    
# analise vulnevabilidades
def banner_analise_vulnevabilidade():
    banner()
    print(f"""{vlh}┃
┃
┃{bra}[ 01 ] SQLiv: scanner massivo de vulnerabilidade de injeção SQL.
{vlh}┃{bra}[ 02 ] sqlscan: Scanner SQL rápido, Dorker, injetor Webshell PHP.
{vlh}┃{bra}[ 03 ] Wordresscan: PScan rewritten in Python + some WPSeku ideas.
{vlh}┃{bra}[ 04 ] WPScan: Scanner de segurança WordPress gratuito.
{vlh}┃{bra}[ 05 ] termux-wordpresscan: ?
{vlh}┃{bra}[ 06 ] TM-scanner: scanner de vulnerabilidade de sites para termux.
{vlh}┃{bra}[ 07 ] Rang3r: Scanner IP + Porta Multi Thread.
{vlh}┃{bra}[ 08 ] Routersploit: Estrutura de exploração para dispositivos incorporados.
{vlh}┃{bra}[ 09 ] SH33LL: Scanner de Shell.
{vlh}┃{bra}[ 10 ] XPL-SEARCH: Pesquise exploits em vários bancos de dados de exploits.
{vlh}┃{bra}[ 11 ] AndroBugs_Framework: Um scanner de vulnerabilidades Android eficiente que ajuda desenvolvedores ou hackers a encontrar possíveis vulnerabilidades de segurança em aplicativos Android.
{vlh}┃{bra}[ 12 ] Clickjacking-Tester: Um script em python projetado para verificar se o site é vulnerável a clickjacking e criar um poc.
{vlh}┗[{bra} 13 {vlh}]{bra} Sn1per: Plataforma de gerenciamento de superfície de ataque | Sn1perSecurity LLC.
""")
    backmenu_inicial()

# ferramenta de web hacking
def banner_web_hacking():
    banner()
    print(f"""{vlh}┃
{vlh}┃{bra}
{vlh}┃{bra}[ 01 ] WebDAV: Explorador de Upload de Arquivos WebDAV.
{vlh}┃{bra}[ 02 ] Webdav Mass Exploiter: Exploração em Massa.
{vlh}┃{bra}[ 03 ] Atlas: Sugestor rápido de táticas para SQLMap.
{vlh}┃{bra}[ 04 ] sqldump: Extrai resultados SQL de sites de forma simples.
{vlh}┃{bra}[ 05 ] Websploit: Um framework avançado de ataque de intermediário (MiTM).
{vlh}┃{bra}[ 06 ] XAttacker: Scanner de Vulnerabilidades de Sites e Explorador Automático.
{vlh}┃{bra}[ 07 ] XSStrike: O mais avançado Scanner de XSS.
{vlh}┃{bra}[ 08 ] Breacher: Um avançado localizador de painéis de administração com múltiplas threads.
{vlh}┃{bra}[ 09 ] ko-dork: Um scanner simples de vulnerabilidades web.
{vlh}┃{bra}[ 10 ] ApSca: Poderosa aplicação de penetração web.
{vlh}┃{bra}[ 11 ] FaDe: Falso desfiguramento com kindeditor, fckeditor e webdav.
{vlh}┃{bra}[ 12 ] xss-payload-list: Lista de Cargas Úteis de Vulnerabilidade de Cross-Site Scripting (XSS).
{vlh}┃{bra}[ 13 ] Xadmin: Localizador de Painéis de Administração.
{vlh}┃{bra}[ 14 ] CMSeeK: Suite de Detecção e Exploração de CMS - Analisa WordPress, Joomla, Drupal e mais de 180 outros CMSs.
{vlh}┃{bra}[ 15 ] CMSmap: Um scanner de código aberto Python para CMSs que automatiza a detecção de falhas de segurança nos CMSs mais populares.
{vlh}┃{bra}[ 16 ] CrawlBox: Forma fácil de forçar a entrada em diretórios da web.
{vlh}┃{bra}[ 17 ] LFISuite: Exploiter LFI (Inclusão de Arquivos Locais) Totalmente Automático (+ Shell Reverso) e Scanner.
{vlh}┃{bra}[ 18 ] Parsero: Ferramenta de auditoria de robots.txt.
{vlh}┃{bra}[ 19 ] Sublist3r: Ferramenta rápida de enumeração de subdomínios para testadores de penetração.
{vlh}┃{bra}[ 20 ] WP-plugin-scanner: Uma ferramenta para listar plugins instalados em um site alimentado por WordPress.
{vlh}┃{bra}[ 21 ] WhatWeb: Scanner web de próxima geração.
{vlh}┃{bra}[ 22 ] fuxploider: Scanner de vulnerabilidades e ferramenta de exploração de upload de arquivos.
{vlh}┗[?]{bra}
""")
    backmenu_inicial()

# 04 - Avaliação do Banco de Dados
def banner_avali_banco_de_dados():
    banner()
    print(f"""{vlh}┃
{vlh}┃{bra}
{vlh}┃{bra}[ 01 ] DbDat: O DbDat realiza inúmeras verificações em um banco de dados para avaliar a segurança
{vlh}┃{bra}[ 02 ] NoSQLMap: Ferramenta automatizada de enumeração de banco de dados NoSQL e exploração de aplicativos web
{vlh}┃{bra}[ 03 ] audit_couchdb: Detecta problemas de segurança, grandes ou pequenos, em um servidor CouchDB
{vlh}┗[?]{bra}    
""")
    backmenu_inicial()

def ferramentas_engenharia_social():
    banner()
    print("""
[ 01 ] DataSocial: Coleta informações de redes sociais por meio de páginas modificadas usando a técnica de phishing com engenharia social.
    """)
    backmenu_inicial()


## {vlh}┣{vlh}
