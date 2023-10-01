"""
SCRIPT RESPONSÁVEL PELA AS LOGOS DO PROJETO
"""

from time import sleep as timeout
import os, sys, time
import urllib.request
from subprocess import check_output as inputstream
import platform as mode
import subprocess

# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" # vermelho 
bra = "\33[1;37m" # branco
az = '\033[34m' # Azul
ma = '\033[35m' # Magento
am = '\033[33m' # Amarelo 
v = "\33[1;36m" # Ciano
b = "\33[1;37m" # branco

# Função para identificar o sistema operacional
# Comando shell que você deseja executar
os.system("cd modules && chmod +x check_distro.sh") ## Dando permissão de execução
comando_shell = "./modules/check_distro.sh"

# Executa o comando shell a partir do arquivo Python
resultado = subprocess.run(comando_shell, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Captura a saída padrão e a saída de erro, se houver
saida = resultado.stdout.decode('utf-8')
erro = resultado.stderr.decode('utf-8')
# Imprime a saída e o erro, se houver
sistema2 = saida
print(erro)


# Função para identificar a arquitetura do dispositivo
def identificar_sistema():
    sistema = mode.system()
    if sistema == "Linux":
        os.system("clear")
        return "Linux"
    elif sistema = mode.system("Arch")
    os.exit()
    else:
        print(f"{vlh}Ferramenta não projetada para esse sistema operacional{bra}")
        sys.exit()

# Função para identificar a arquitetura do dispositivo
def identificar_arquitetura():
    arquitetura = mode.architecture()[0]
    return arquitetura


# Função principal
def banner_inicial():
    os.system("clear")
    sistema = identificar_sistema()
    arquitetura = identificar_arquitetura()
    
    ## banner de apresentação das categorias
    print(f"""
    
{ma}--+=[ {am}Sistema: {sistema2}
{ma}--+=[ {am}Arquitetura: {arquitetura} - {mode.machine()}
{ma}--+=[ {am}Versão python: {mode.python_version()}
{vd} ▄{vlh}█          ▄████████  ▄███████▄  ▄██   ▄
{vd}███  {vlh}       ███    ███ ██▀     ▄██ ███   ██▄
{vd}███     {vlh}    ███    ███       ▄███▀ ███▄▄▄███
{vd}███         {vlh}███    ███  ▀█▀▄███▀▄▄ ▀▀▀▀▀▀███
{vd}███       ▀████{vlh}███████   ▄███▀   ▀ ▄██   ███
{vd}███         ███    ███{vlh} ▄███▀       ███   ███
{vd}███▌    ▄   ███    ███ ██{vlh}█▄     ▄█ ███   ███
{vd}█████▄▄██   ███    █▀   ▀███{vlh}█████▀  ▀█████▀
{bra}+=[ By: AstralSec{vlh}Haxor {bra}-- AlcaX ]=+                              
{vd}               ███    █▄     ▄██████{vlh}██    ▄████████    ▄████████ 
{vd}               ███    ███   ███    ███   {vlh}███    ███   ███    ███ 
{vd}               ███    ███   ███    █▀    ███ {vlh}   █▀    ███    ███ 
{vd}               ███    ███   ███         ▄███▄▄▄ {vlh}     ▄███▄▄▄▄██▀ 
{vd}               ███    ███ ▀███████████ ▀▀███▀▀▀     {vlh}▀▀███▀▀▀▀▀   
{vd}               ███    ███          ███   ███    █▄  ▀███{vlh}████████ 
{vd}               ███    ███    ▄█    ███   ███    ███   ███  {vlh}  ███ 
{vd}               ████████▀   ▄████████▀    ██████████   ███    {vlh}███ 
{bra}   Selecione categoria da sua ferramenta preferida :) {vd}███    {vlh}███
{bra}     _________________________________________________{vd}███____█{vlh}██
{bra}    /                                                 {vd}███    ██{vlh}█
{bra}    |[ 01 ] Coletar de Informações                           |
    |                                                         |
    |[ 02 ] Análise de Vulnerabilidades                      |
    |                                                         |
    |[ 03 ] Web Hacking                                      |
    |                                                         |
    |[ 04 ] Avaliações de Banco de Dados                     |
    |                                                         |
    |[ 05 ] Ataques de Senha                                 |
    |                                                         |
    |[ 06 ] Ataques Sem Fio                                  |
    |                                                         |
    |[ 07 ] Engenharia Reversa                               |
    |                                                         |
    |[ 08 ] Ferramentas de Exploração                        |
    |                                                         |
    |[ 09 ] Sniffing e Spoofing                              |
    |                                                         |
    |[ 10 ] Ferramentas de Relatórios                        |
    |                                                         |
    |[ 11 ] Ferramentas de Forenses                          |
    |                                                         |
    |[ 12 ] Teste de Estresse                                |
    |                                                         |
    |[ 13 ] Instalar Distribuições Linux                     |
    |                                                         |
    |[ 14 ] Utilitário Termux                                |
    |                                                         |
    |[ 15 ] Análise de Malware                               |
    |                                                         |
    |[ 16 ] Ferramentas de Engenharia Social                 |
    |                                                         |
    |                                                        |
    |                                                         |
    |                                                        |
    |                                                         |
    |                                                        |
    |                                                         |
    |                                                        |
    |[ X ] ~> Atualização                                     |
    |[ 00 ] ~> Sair da LazyUser    __________________________/
    \_____________________________/

""")

if __name__ == "__main__":
    banner_inicial()


def banner(): ## banner de apresentação do menu de opções do tool
    os.system("clear")
    print(f"""
{vd} █{vlh}████
{vd}░░██{vlh}█
{vd} ░███ {vlh}        ██████    █████████ █████ ████
{vd} ░███   {vlh}     ░░░░░███  ░█░░░░███ ░░███ ░███
{vd} ░███       {vlh}  ███████  ░   ███░   ░███ ░███
{vd} ░███      █ █{vlh}██░░███    ███░   █ ░███ ░███
{vd} ███████████░░██{vlh}██████  █████████ ░░███████
{vd}░░░░░░░░░░░  ░░░░░{vlh}░░░  ░░░░░░░░░   ░░░░░███
{vd}                    {vlh}     ░░░░░     ███ ░███
{vd}                      {vlh}   ░         ░░██████   
{bra}+=[ By: AstralSec{vlh}Haxor {bra}-- AlcaX ]=+{vlh}░░░░░░
{vd}            ███    █▄     {vlh}▄████████░░░████████    ▄████████ 
{vd}            ███    ███   ███{vlh}    ███░░ ███    ███   ███    ███ 
{vd}            ███    ███   ███   {vlh} █▀ ░  ███    █▀    ███    ███ 
{vd}            ███    ███   ███      {vlh}   ▄███▄▄▄      ▄███▄▄▄▄██▀ 
{vd}            ███    ███ ▀███████████ {vlh}▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
{vd}            ███    ███          ███   █{vlh}██    █▄  ▀███████████ 
{vd}            ███    ███    ▄█    ███   ███ {vlh}   ███   ███    ███ 
{vd}            ████████▀   ▄████████▀    ████████{vlh}██   ███    ███ 
    {am}Escolha a opção da sua ferramenta preferida :) {vd}█{vlh}██    ███
{bra}___________________________________________________{vd}███{vlh}{bra}____{vlh}███{bra}___________________
                                                   {vd}███  {vlh}  ███
{bra}""")



    ## banner de instalação das ferramentas.
def install_banner():
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


    ## banner de verificação ser a ferramenta já existente em algum diretório.
def Installed_banner(): 
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
def backmenu(): ## menu de opções para voltar ao menu  anterior ou sair 
    print(f"""{v}
    [ enter ] ~> Voltar ao menu anterior.
    [ 00 ] ~> Sair da LazyUser.
    {b}
 """)
 
 
def backmenu_inicial(): ## menu de opções para voltar ao menu inicial ou sair
    print(f"""{v}
    [ enter ] ~> Voltar ao menu Inicial.
    [ 00 ] ~> Sair da LazyUser.
""")


def sair_do_programar(): ## Sair do script
    print(f"\n\n{v}Você saiu da LazyUser !{b}\n")
    sys.exit()

def atualizar(): ## Fazer atualização  ao script
    os.system("git pull")
