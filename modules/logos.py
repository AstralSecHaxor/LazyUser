from time import sleep as timeout
import os, sys, time
import urllib.request
from subprocess import check_output as inputstream

## cores
vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" # vermelho 
bra = "\33[1;37m" # branco
az = '\033[34m' # Azul
ma = '\033[35m' # Magento
am = '\033[33m' # Amarelo 
v = "\33[1;36m" # Ciano
b = "\33[1;37m" # branco


def banner_inicial(): ## Banner das categorias.
    os.system("clear")
    print(f"""

{vd} ▄{vlh}█          ▄████████  ▄███████▄  ▄██   ▄
{vd}███  {vlh}       ███    ███ ██▀     ▄██ ███   ██▄
{vd}███     {vlh}    ███    ███       ▄███▀ ███▄▄▄███
{vd}███         {vlh}███    ███  ▀█▀▄███▀▄▄ ▀▀▀▀▀▀███{am}+- -- +=[ Author: AlcaX
{vd}███       ▀████{vlh}███████   ▄███▀   ▀ ▄██   ███{am}+- -- +=[ Team: A.S.H AstralSecHaxor
{vd}███         ███    ███{vlh} ▄███▀       ███   ███{am}+- -- +=[ Version: 1.0 - beta
{vd}███▌    ▄   ███    ███ ██{vlh}█▄     ▄█ ███   ███{am}+- -- +=[ Channel: @AstralSec_Haxor
{vd}█████▄▄██   ███    █▀   ▀███{vlh}█████▀  ▀█████▀ 
{vd}                                  {vlh}                              
{vd}               ███    █▄     ▄██████{vlh}██    ▄████████    ▄████████ 
{vd}               ███    ███   ███    ███   {vlh}███    ███   ███    ███ 
{vd}               ███    ███   ███    █▀    ███ {vlh}   █▀    ███    ███ 
{vd}               ███    ███   ███         ▄███▄▄▄ {vlh}     ▄███▄▄▄▄██▀ 
{vd}               ███    ███ ▀███████████ ▀▀███▀▀▀     {vlh}▀▀███▀▀▀▀▀   
{vd}               ███    ███          ███   ███    █▄  ▀███{vlh}████████ 
{vd}               ███    ███    ▄█    ███   ███    ███   ███  {vlh}  ███ 
{vd}               ████████▀   ▄████████▀    ██████████   ███    {vlh}███ 
{bra}     _________________________________________________{vd}███____█{vlh}██
{bra}    /                                                 {vd}███    ██{vlh}█
{bra}    |[ 01 ] Coletar de Informações                            |
    |                                                        |
    |[ 02 ] Análise de Vulnerabilidades                       |
    |                                                        |
    |[ 03 ] Web Hacking                                       |
    |                                                        |
    |[ 04 ] Avaliações de Danco de Dados                      |
    |                                                        |
    |[ 05 ] Ataques de Senha                                  |
    |                                                        |
    |[ 06 ] Ataques sem Fio                                   |
    |                                                        |
    |[ 07 ] Engenharia Reversa                                |
    |                                                        |
    |[ 08 ] Ferramentas de Exploração                         |
    |                                                        |
    |[ 09 ] Sniffing e Spoofing                               |
    |                                                        |
    |[ 10 ] Ferramentas de Relatórios                         |
    |                                                        |
    |[ 11 ] Ferramentas de Forenses                           |
    |                                                        |
    |[ 12 ] Teste de Estresse                                 |
    |                                                        |
    |[ 13 ] Instalar Distribuições Linux                      |
    |                                                        |
    |[ 14 ] Utilitário Termux                                 |
    |                                                        |
    |[ 15 ] Análise de Malware                                |
    |                                                        |
    |[ 16 ] Ferramentas de Engenharia Social                  |
    |                                                        |
    |                                                         |
    |[ Off ]  Shell Reverse                                  |
    |                                                         |
    |                                                        |
    |                                                         |
    |                                                        |
    |[ 90 ] ~> Acrescentado             [ X ] -> Atualização  |
    |[ 00 ] ~> Sair da LazyUser         _____________________/
     \_________________________________/

    """)


def banner(): ## banner de apresentação do menu de opções do tool
    os.system("clear")
    print(f"""
{vd} █{vlh}████
{vd}░░██{vlh}█
{vd} ░███ {vlh}        ██████    █████████ █████ ████
{vd} ░███   {vlh}     ░░░░░███  ░█░░░░███ ░░███ ░███
{vd} ░███       {vlh}  ███████  ░   ███░   ░███ ░███
{vd} ░███      █ █{vlh}██░░███    ███░   █ ░███ ░███{am}+- -- +=[ Author: AlcaX
{vd} ███████████░░██{vlh}██████  █████████ ░░███████{am}+- -- +=[ Team: A.S.H AstralSecHaxor
{vd}░░░░░░░░░░░  ░░░░░{vlh}░░░  ░░░░░░░░░   ░░░░░███{am}+- -- +=[ Version: 1.0 - beta
{vd}                    {vlh}     ░░░░░     ███ ░███{am}+- -- +=[ Channel: @AstralSec_Haxor
{vd}                      {vlh}   ░         ░░██████   
{vd}                        {vlh}           ░░░░░░
{vd}            ███    █▄     {vlh}▄████████░░░████████    ▄████████ 
{vd}            ███    ███   ███{vlh}    ███░░ ███    ███   ███    ███ 
{vd}            ███    ███   ███   {vlh} █▀ ░  ███    █▀    ███    ███ 
{vd}            ███    ███   ███      {vlh}   ▄███▄▄▄      ▄███▄▄▄▄██▀ 
{vd}            ███    ███ ▀███████████ {vlh}▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
{vd}            ███    ███          ███   █{vlh}██    █▄  ▀███████████ 
{vd}            ███    ███    ▄█    ███   ███ {vlh}   ███   ███    ███ 
{vd}            ████████▀   ▄████████▀    ████████{vlh}██   ███    ███ 
    {am}Escolha a opção da sua ferramenta preferida :) {vd}█{vlh}██    ███
{bra}___________________________________________________{vd}███{vlh}{bra}____{vlh}███{bra}____________________
                                                   {vd}███  {vlh}  ███
{bra}""")

def install_banner(): ## banner de instalação das ferramentas.
    os.system("clear")
    print(f"""{ma}
.------------------------------------------------------------------------.
 )                                                                      (
(    {vd}       ___           _        _                 _           {ma}        )
 )   {vd}      |_ _|_ __  ___| |_ __ _| | __ _ _ __   __| | ___      {ma}       (
(    {vd}       | || '_ \/ __| __/ _` | |/ _` | '_ \ / _` |/ _ \     {ma}        )
 )   {vd}       | || | | \__ \ || (_| | | (_| | | | | (_| | (_) |    {ma}       (
(    {vd}      |___|_| |_|___/\__\__,_|_|\__,_|_| |_|\__,_|\___/ ••• {ma}        )
 )   {vd}                                                            {ma}       (
'------------------------------------------------------------------------'
    """)


def Installed_banner(): ## banner de verificação ser a ferramenta já existente em algum diretório.
    os.system("clear")
    print(f"""{ma}
.----------------------------------------------------------------.
 )                                                              (
(      {vlh}     ___           _        _           _       {ma}          )
 )     {vlh}    |_ _|_ __  ___| |_ __ _| | __ _  __| | ___   {ma}        (
(      {vlh}     | || '_ \/ __| __/ _` | |/ _` |/ _` |/ _ \  {ma}         )
 )     {vlh}     | || | | \__ \ || (_| | | (_| | (_| | (_) | {ma}        (
(      {vlh}    |___|_| |_|___/\__\__,_|_|\__,_|\__,_|\___/   {ma}        )
 )                                                             {ma} (
(               {vd}[ enter ] ~> Voltar ao menu anterior.     {ma}       )
 )              {vd}[ 00 ] ~> Sair da LazyUser.               {ma}      (
'----------------------------------------------------------------'""")

    
# BANNERS DE OPÇÕES DE NAVEGAR PELO SCRIPT
def backmenu(): ## menu da category Coletar de vulnerabilidades
    print(f"""{v}
    [ enter ] ~> Voltar ao menu anterior.
    [ 00 ] ~> Sair da LazyUser.
    {b}
 """)
 
 
def backmenu_inicial(): ## menu de opções para voltar ao menu inicial
    print(f"""{v}
    [ enter ] ~> Voltar ao menu Inicial.
    [ 00 ] ~> Sair da LazyUser.
""")


def sair_do_programar(): ## Sair do script
    print(f"\n\n{v}Você saiu da LazyUser !{b}\n")
    sys.exit()

def atualizar(): ## Fazer atualização  ao script
    os.system("git pull")
