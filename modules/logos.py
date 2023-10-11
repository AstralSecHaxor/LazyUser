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
    return "Sistema não identificado"

sistema_atual = verificar_sistema()

# Função para identificar a arquitetura do dispositivo
def identificar_sistema():
    sistema = mode.system()
    if sistema == "Linux":
        os.system("clear")
        return "Linux"
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
    
{ma}--+=[ {bra}Sistema:{az} {sistema_atual}
{ma}--+=[ {bra}Arquitetura:{az} {arquitetura} {bra}-{az} {mode.machine()}
{ma}--+=[ {bra}Versão Python:{az} {mode.python_version()}
{vd} ▄{vlh}█          ▄████████  ▄███████▄  ▄██   ▄
{vd}███  {vlh}       ███    ███ ██▀     ▄██ ███   ██▄
{vd}███     {vlh}    ███    ███       ▄███▀ ███▄▄▄███
{vd}███         {vlh}███    ███  ▀█▀▄███▀▄▄ ▀▀▀▀▀▀███
{vd}███       ▀████{vlh}███████   ▄███▀   ▀ ▄██   ███
{vd}███         ███    ███{vlh} ▄███▀       ███   ███
{vd}███▌    ▄   ███    ███ ██{vlh}█▄     ▄█ ███   ███
{vd}█████▄▄██   ███    █▀   ▀███{vlh}█████▀  ▀█████▀
{bra}+=[ By: AstralSec{vlh}Haxor {bra}-- ALLi{vlh}Sec {bra}]=+                              
{vd}               ███    █▄     ▄██████{vlh}██    ▄████████    ▄████████ 
{vd}               ███    ███   ███    ███   {vlh}███    ███   ███    ███ 
{vd}               ███    ███   ███    █▀    ███ {vlh}   █▀    ███    ███ 
{vd}               ███    ███   ███         ▄███▄▄▄ {vlh}     ▄███▄▄▄▄██▀ 
{vd}               ███    ███ ▀███████████ ▀▀███▀▀▀     {vlh}▀▀███▀▀▀▀▀   
{vd}               ███    ███          ███   ███    █▄  ▀███{vlh}████████ 
{vd}               ███    ███    ▄█    ███   ███    ███   ███  {vlh}  ███ 
{vd}               ████████▀   ▄████████▀    ██████████   ███    {vlh}███ 
{bra}   {am}Selecione categoria da sua ferramenta preferida :) {vd}███    {vlh}███
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
    |                   atualizando 555                                      |
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

def banner_coletar_informacoes():
    os.system("clear")
    banner()
    print("""
[ 01 ] Nmap: Utilitário para descoberta de rede e auditoria de segurança.
[ 02 ] Red Hawk: Coleta de informações, verificação de vulnerabilidades e rastreamento.
[ 03 ] D-TECT: Ferramenta multifuncional para testes de penetração.
[ 04 ] sqlmap: Ferramenta automática de injeção SQL e controle de banco de dados.
[ 05 ] ReconDog: Ferramenta de coleta de informações e verificação de vulnerabilidades.
[ 06 ] AndroZenmap: ?
[ 07 ] sqlmate: Um amigo do SQLmap que fará o que você sempre esperou do SQLmap.
[ 08 ] AstraNmap: Verificador de segurança usado para localizar hosts e serviços em uma rede de computadores.
[ 09 ] MapEye: Rastreador de localização GPS preciso Android, IOS, Windows phones.
[ 10 ] Easymap: Atalho do Nmap.
[ 11 ] Crips: Esta ferramenta é uma coleção de ferramentas IP on-line que podem ser usadas para obter rapidamente informações sobre endereços IP, páginas da Web e registros DNS.
[ 12 ] EvilURL: Gere domínios malignos unicode para ataque homógrafo de IDN e detecte-os.
[ 13 ] Striker: Conjunto de verificação de reconhecimento e vulnerabilidade.
[ 14 ] Xshell: Conjunto de ferramentas (ToolKit).
[ 15 ] OWScan: Verificador da Web OVID.
[ 16 ] OSIF: Informações de código aberto Facebook.
[ 17 ] Namechk: Ferramenta OSINT baseada em namechk.com para verificar nomes de usuários em mais de 100 sites, fóruns e redes sociais.
[ 18 ] AUXILE: Estrutura de análise de aplicativos da Web.
[ 19 ] inther: Coleta de informações usando shodan, censys e hackertarget.
[ 20 ] GINF: Ferramenta de coleta de informações do GitHub.
[ 21 ] GPS Tracking: ?
[ 22 ] ASU: Kit de ferramentas para hackear o Facebook.
[ 23 ] fim: Downloader de imagens do Facebook.
[ 24 ] pwnedOrNot: Ferramenta OSINT para encontrar senhas de contas de e-mail comprometidas.
[ 25 ] dnsrecon: Avaliação de segurança e solução de problemas de rede.
[ 26 ] zphisher: Ferramenta automatizada de phishing.
[ 27 ] Mr.SIP: Ferramenta de auditoria e ataque baseada em SIP.
[ 28 ] userrecon: Encontre nomes de usuário em mais de 75 redes sociais.
[ 29 ] PhoneInfoga: Uma das ferramentas mais avançadas para escanear números de telefone usando apenas recursos gratuitos.
[ 30 ] SiteBroker: Um utilitário multiplataforma baseado em python para coleta de informações e automação de testes de penetração.
[ 31 ] GatheTOOL: Coleta de informações - API hackertarget.com
[ 32 ] ADB-ToolKit: ?
[ 33 ] TekDefense-Automater: Automater - URL IP e análise MD5 OSINT.
[ 34 ] EagleEye: Persiga seus amigos. Encontre seus perfis do Instagram, FB e Twitter usando reconhecimento de imagens e pesquisa reversa de imagens.
[ 35 ] EyeWitness: EyeWitness foi projetado para fazer capturas de tela de sites, fornecer algumas informações de cabeçalho do servidor e identificar credenciais padrão, se possível.
[ 36 ] InSpy: Uma ferramenta de enumeração do LinkedIn baseada em python.
[ 37 ] fierce: Uma ferramenta de reconhecimento de DNS para localizar espaço IP não contíguo.
[ 38 ] gasmask: Ferramenta de coleta de informações - OSINT.
""")
    backmenu_inicial()


def banner_analise_vulnevabilidade():
    os.system("clear")
    banner()
    print("""
[ 01 ] SQLiv: scanner massivo de vulnerabilidade de injeção SQL.
[ 02 ] sqlscan: Scanner SQL rápido, Dorker, injetor Webshell PHP.
[ 03 ] Wordresscan: PScan rewritten in Python + some WPSeku ideas.
[ 04 ] WPScan: Scanner de segurança WordPress gratuito.
[ 05 ] termux-wordpresscan: ?
[ 06 ] TM-scanner: scanner de vulnerabilidade de sites para termux.
[ 07 ] Rang3r: Scanner IP + Porta Multi Thread.
[ 08 ] Routersploit: Estrutura de exploração para dispositivos incorporados.
[ 09 ] SH33LL: Shell Scanner.
[ 10 ] XPL-SEARCH: Pesquise exploits em vários bancos de dados de exploits.
[ 11 ] AndroBugs_Framework: Um scanner de vulnerabilidades Android eficiente que ajuda desenvolvedores ou hackers a encontrar possíveis vulnerabilidades de segurança em aplicativos Android.
[ 12 ] Clickjacking-Tester: Um script em python projetado para verificar se o site é vulnerável a clickjacking e criar um poc.
[ 13 ] Sn1per: Plataforma de gerenciamento de superfície de ataque | Sn1perSecurity LLC.
""")
    backmenu_inicial()




def banner(): ## banner de apresentação do menu de opções do tool
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
{bra}+=[ By: AstralSec{vlh}Haxor {bra}-- ALLi{vlh}Sec {bra}]=+{vlh}░░░░░░
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
'------------------------------------------------------------------------'""")



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
(                                                         {ma}       )
 )                                                        {ma}      (
'----------------------------------------------------------------'
""")
    
# BANNERS DE OPÇÕES DE NAVEGAR PELO SCRIPT
def backmenu(): ## menu de opções para voltar ao menu  anterior ou sair 
    print(f"""
    {bra}[ {vlh}enter {bra}] ~> {v}Voltar ao menu anterior.
    {bra}[ {vlh}00 {bra}] ~> {v}Sair da LazyUser.
 """)
 
 
def backmenu_inicial(): ## menu de opções para voltar ao menu inicial ou sair
    print(f"""{bra}
   [ {vlh}enter {bra}] ~> {v}Voltar ao menu Inicial.
   {bra}[ {vlh}00 {bra}] ~> {v}Sair da LazyUser.
   {bra}[ {vlh}multi install{bra} ] ~> {v}Faça uma sequência de opções separadas por vírgulas.
      {am}Ex{bra}: 3,23,6,19
""")


def sair_do_programar(): ## Sair do script
    print(f"\n\n{v}Você saiu da LazyUser !{b}\n")
    sys.exit()

    ## Fazer atualização  ao script
def atualizar(): 
    
    # Define o diretório de instalação
    installation_dir = "/usr/bin/LazyUser"  # Substitua pelo caminho correto da sua ferramenta
    
    # Verifica se o diretório de instalação existe
    if os.path.exists(installation_dir):
        # Acesse o diretório de instalação
        os.chdir(installation_dir)
    
        # Tente atualizar o repositório com os arquivos mais recentes
        pull_result = subprocess.run(["git", "pull"], capture_output=True, text=True)
    
        if pull_result.returncode == 0:
            # Verifique se a saída do "git pull" contém "Already up to date"
            if "Already up to date" in pull_result.stdout:
                print("Nada para atualizar. O repositório já está atualizado.")
            else:
                print("Atualização bem-sucedida.")
    
                # Torna o script "install.sh" executável (se necessário)
                subprocess.run(["chmod", "+x", "install.sh"])
    
                # Executa o script "install.sh" (se necessário)
                #subprocess.run(["bash", "install.sh"])
        else:
            print("Erro ao atualizar o repositório.")
    else:
        print("Diretório de instalação não encontrado. Certifique-se de que o diretório esteja correto.")
