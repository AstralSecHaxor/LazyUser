## Banco da Categoria análise de vulnerabilidades

import os
from modules.logos import *
from os.path import exists


vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" #vermelho 
bra = "\33[1;37m" # branco
az = '\033[34m' # Azul
ma = '\033[35m' #Magento
am = '\033[33m' #Amarelo 

Dirbin= "/data/data/com.termux/files/usr/bin"
#variável com caminho até o diretório home
CasaDir = "/data/data/com.termux/files/home"


def analisevuln():
    banner()
    analisevulnxx = open("modules/banners/analisevuln")
    print(analisevulnxx.read())
    backmenu_inicial()


def sqliv():
	if os.path.exists(f"{CasaDir}/sqliv") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/sqliv") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> SQLiv')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('git clone https://github.com/the-robot/sqliv')
	    os.system('mv sqliv {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()


def sqlscan():
	if os.path.exists(f"{CasaDir}/sqlscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/sqlscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> sqlscan')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php')
	    os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	    os.system('mv sqlscan {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def wordpreSScan():
	if os.path.exists(f"{CasaDir}/Wordpresscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Wordpresscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Wordpresscan')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	    os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	    os.system('mv Wordpresscan {}'.format(CasaDir))
	    os.system('cd {}/Wordpresscan && python2 -m pip install -r requirements.txt'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()
	
def wpscan():
	if os.path.exists(f"{CasaDir}/wpscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/wpscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> WPScan')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git ruby curl')
	    os.system('git clone https://github.com/wpscanteam/wpscan')
	    os.system('mv wpscan {0} && cd {0}/wpscan'.format(CasaDir))
	    os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def wordpresscan():
	if os.path.exists(f"{CasaDir}/termux-wordpresscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/termux-wordpresscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> termux-wordpresscan')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install nmap figlet git')
	    os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	    os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	    os.system('mv termux-wordpresscan {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def tmscanner():
	if os.path.exists(f"{CasaDir}/Wordpresscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Wordpresscan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> TM-scanner')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python python2 nmap git -y')
	    os.system('python -m pip install colorama requests')
	    os.system('python2 -m pip install colorama requests')
	    os.system('git clone https://github.com/TechnicalMujeeb/TM-scanner')
	    os.system('mv TM-scanner {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def rang3r():
	if os.path.exists(f"{CasaDir}/rang3r") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/rang3r") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Rang3r')
	    os.system("apt update && apt upgrade")
	    os.system("apt install git python2 && python2 -m pip install optparse termcolor")
	    os.system("git clone https://github.com/floriankunushevci/rang3r")
	    os.system("mv rang3r {}".format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def routersploit():
	if os.path.exists(f"{CasaDir}/routersploit") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/routersploit") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Routersploit')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('python2 -m pip install requests')
	    os.system('git clone https://github.com/threat9/routersploit')
	    os.system('mv routersploit {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def sh33ll():
	if os.path.exists(f"{CasaDir}/SH33LL") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/SH33LL") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> SH33LL')
	    os.system("apt update && apt upgrade")
	    os.system("apt install git python2")
	    os.system("git clone https://github.com/LOoLzeC/SH33LL")
	    os.system("mv SH33LL {}".format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def xattacker():
	if os.path.exists(f"{CasaDir}/XAttacker") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/XAttacker") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> XAttacker')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git perl')
	    os.system('cpnm install HTTP::Request')
	    os.system('cpnm install LWP::Useragent')
	    os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	    os.system('mv XAttacker {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def xplsearch():
	if os.path.exists(f"{CasaDir}/XPL-SEARCH") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/XPL-SEARCH") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> XPL-SEARCH')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php -y')
	    os.system('git clone https://github.com/r00tmars/XPL-SEARCH')
	    os.system('mv XPL-SEARCH {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def androbugs():
	if os.path.exists(f"{CasaDir}/AndroBugs_Framework") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/AndroBugs_Framework") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> AndroBugs_Framework')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 -y')
	    os.system('python2 -m pip install pymongo')
	    os.system('git clone https://github.com/AndroBugs/AndroBugs_Framework')
	    os.system('mv AndroBugs_Framework {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def clickjacking():
	if os.path.exists(f"{CasaDir}/Clickjacking-Tester") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Clickjacking-Tester") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Clickjacking-Tester')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('git clone https://github.com/D4Vinci/Clickjacking-Tester')
	    os.system('mv Clickjacking-Tester {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def sn1per():
	if os.path.exists(f"{CasaDir}/Sn1per") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Sn1per") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Sn1per')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('git clone https://github.com/1N3/Sn1per')
	    os.chdir("Sn1per")
	    os.system("bash install.sh")
	    os.chdir("..")
	    os.system('mv Sn1per {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()
