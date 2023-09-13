## Banco da Categoria coletar de informações

import os
from modules.logos import *
from os.path import exists

vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" #vermelho 
bra = "\33[1;37m" # branco
az = '\033[34m' # Azul
ma = '\033[35m' #Magento
am = '\033[33m' #Amarelo 

def coleinfox(): ## banner da category coleta de informações
    banner()
    coleinfoxx = open("modules/banners/coletainfox")
    print(coleinfoxx.read())
    backmenu_inicial()


Dirbin= "/data/data/com.termux/files/usr/bin"
#variável com caminho até o diretório home
CasaDir = "/data/data/com.termux/files/home"


def nmap():
    if os.path.exists(f"{CasaDir}/nmap") == True:
        Installed_banner()
        print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
    elif os.path.exists(f"{Dirbin}/nmap") == True:
        Installed_banner()
        print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
    else:
	    install_banner()
	    print(f'{v}INSTALANDO --> Nmap')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install nmap')
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()
	
def red_hawk():
    if os.path.exists(f"{CasaDir}/RED_HAWK") == True:
        Installed_banner()
        print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
    elif os.path.exists(f"{Dirbin}/RED_HAWK") == True:
        Installed_banner()
        print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
    else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> RED HAWK')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php')
	    os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	    os.system('mv RED_HAWK {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def dtect():
	if os.path.exists(f"{CasaDir}/D-TECT") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/D-TECT") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> D-TECT')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('git clone https://github.com/bibortone/D-Tech')
	    os.system('mv D-Tech {}/D-TECT'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def sqlmap():
	if os.path.exists(f"{CasaDir}/sqlmap") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/sqlmap") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> sqlmap')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2')
	    os.system('git clone https://github.com/sqlmapproject/sqlmap')
	    os.system('mv sqlmap {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def infoga():
	if os.path.exists(f"{CasaDir}/Infoga") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Infoga") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Infoga')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('python2 -m pip install requests urllib3 urlparse')
	    os.system('git clone https://github.com/m4ll0k/Infoga')
	    os.system('mv Infoga {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def reconDog():
	if os.path.exists(f"{CasaDir}/ReconDog") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/ReconDog") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> ReconDog')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('git clone https://github.com/s0md3v/ReconDog')
	    os.system('mv ReconDog {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def androZenmap():
	if os.path.exists(f"{CasaDir}/AndroZenmap") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/AndroZenmap") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> AndroZenmap')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install nmap curl')
	    os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	    os.system('mkdir {}/AndroZenmap'.format(CasaDir))
	    os.system('mv androzenmap.sh {}/AndroZenmap'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def sqlmate():
	if os.path.exists(f"{CasaDir}/sqlmate") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/sqlmate") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> sqlmate')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git')
	    os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
	    os.system('git clone https://github.com/s0md3v/sqlmate')
	    os.system('mv sqlmate {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def astraNmap():
	if os.path.exists(f"{CasaDir}/AstraNmap") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/AstraNmap") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> AstraNmap')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git nmap')
	    os.system('git clone https://github.com/Gameye98/AstraNmap')
	    os.system('mv AstraNmap {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def mapeye():
	if os.path.exists(f"{CasaDir}/MapEye") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/MapEye") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> MapEye')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php python -y')
	    os.system('python -m pip install requests')
	    os.system('git clone https://github.com/bhikandeshmukh/MapEye')
	    os.system('mv MapEye {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def easyMap():
	if os.path.exists(f"{CasaDir}/Easymap") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Easymap") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Easymap')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install php git')
	    os.system('git clone https://github.com/Cvar1984/Easymap')
	    os.system('mv Easymap {}'.format(CasaDir))
	    os.system('cd {}/Easymap && sh install.sh'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def blackbox():
	if os.path.exists(f"{CasaDir}/blackbox") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/blackbox") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> BlackBox')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git && python2 -m pip install optparse passlib')
	    os.system('git clone https://github.com/jothatron/blackbox')
	    os.system('mv blackbox {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()
	    
def crips():
	if os.path.exists(f"{CasaDir}/Crips") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Crips") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Crips')
	    os.system("apt update && apt upgrade")
	    os.system("apt install git python2 openssl curl libcurl wget")
	    os.system("git clone https://github.com/Manisso/Crips")
	    os.system("mv Crips {}".format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def sir():
	if os.path.exists(f"{CasaDir}/sir") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/sir") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> SIR')
	    os.system("apt update && apt upgrade")
	    os.system("apt install python2 git")
	    os.system("python2 -m pip install bs4 urllib2")
	    os.system("git clone https://github.com/AeonDave/sir.git")
	    os.system("mv sir {}".format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def evilURL():
	if os.path.exists(f"{CasaDir}/EvilURL") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/EvilURL") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> EvilURL')
	    os.system("apt update && apt upgrade")
	    os.system("apt install git python2 python3")
	    os.system("git clone https://github.com/UndeadSec/EvilURL")
	    os.system("mv EvilURL {}".format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def striker():
	if os.path.exists(f"{CasaDir}/Striker") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Striker") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Striker')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2')
	    os.system('git clone https://github.com/s0md3v/Striker')
	    os.system('mv Striker {}'.format(CasaDir))
	    os.system('cd /Striker && python2 -m pip install -r requirements.txt'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def xshell():
	if os.path.exists(f"{CasaDir}/Xshell") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Xshell") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Xshell')
	    os.system("apt update && apt upgrade")
	    os.system("apt install lynx python2 figlet ruby php nano w3m")
	    os.system("git clone https://github.com/Ubaii/Xshell")
	    os.system("mv Xshell {}".format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def owscan():
	if os.path.exists(f"{CasaDir}/OWScan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/OWScan") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> OWScan')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php')
	    os.system('git clone https://github.com/Gameye98/OWScan')
	    os.system('mv OWScan {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def osif():
	if os.path.exists(f"{CasaDir}/OSIF") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/OSIF") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> OSIF')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2')
	    os.system('python2 -m pip install requests')
	    os.system('git clone https://github.com/CiKu370/OSIF')
	    os.system('mv OSIF {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def devploit():
	if os.path.exists(f"{CasaDir}/Devploit") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Devploit") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Devploit')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python2 git && python2 -m pip install urllib2')
	    os.system('git clone https://github.com/joker25000/Devploit')
	    os.system('mv Devploit {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def namechk():
	if os.path.exists(f"{CasaDir}/Namechk") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Namechk") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Namechk')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git')
	    os.system('git clone https://github.com/HA71/Namechk')
	    os.system('mv Namechk {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def auxile():
	if os.path.exists(f"{CasaDir}/AUXILE") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/AUXILE") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> AUXILE')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	    os.system('git clone https://github.com/CiKu370/AUXILE')
	    os.system('mv AUXILE {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def inther():
	if os.path.exists(f"{CasaDir}/inther") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/inther") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> inther')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git ruby')
	    os.system('git clone https://github.com/Gameye98/inther')
	    os.system('mv inther {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def ginf():
	if os.path.exists(f"{CasaDir}/GINF") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/GINF") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> GINF')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php')
	    os.system('git clone https://github.com/Gameye98/GINF')
	    os.system('mv GINF {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def gpstr():
	if os.path.exists(f"{CasaDir}/gps_tracking") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/gps_tracking") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> GPS Tracking')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install php git')
	    os.system('git clone https://github.com/indosecid/gps_tracking')
	    os.system('mv gps_tracking {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def asu():
	if os.path.exists(f"{CasaDir}/ASU") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/ASU") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> ASU')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 php')
	    os.system('python2 -m pip install requests bs4 mechanize')
	    os.system('git clone https://github.com/LOoLzeC/ASU')
	    os.system('mv ASU {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def fim():
	if os.path.exists(f"{CasaDir}/fim") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/fim") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> fim')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python && python -m pip install requests bs4')
	    os.system('git clone https://github.com/karjok/fim')
	    os.system('mv fim {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def maxsubdofinder():
	if os.path.exists(f"{CasaDir}/MaxSubdoFinder") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/MaxSubdoFinder") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> MaxSubdoFinder')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2')
	    os.system('python2 -m pip install requests')
	    os.system('git clone https://github.com/maxteroit/MaxSubdoFinder')
	    os.system('mv MaxSubdoFinder {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def pwnedOrNot():
	if os.path.exists(f"{CasaDir}/pwnedOrNot") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/pwnedOrNot") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> pwnedOrNot')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python')
	    os.system('python -m pip install requests')
	    os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
	    os.system('mv pwnedOrNot {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def maclook():
	if os.path.exists(f"{CasaDir}/Mac-Lookup") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Mac-Lookup") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Mac-Lookup')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python')
	    os.system('python -m pip install requests')
	    os.system('git clone https://github.com/T4P4N/Mac-Lookup')
	    os.system('mv Mac-Lookup {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def billcypher():
	if os.path.exists(f"{CasaDir}/BillCypher") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/BillCypher") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> BillCypher')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python')
	    os.system('python -m pip install argparse dnspython requests urllib3 colorama')
	    os.system('git clone https://github.com/GitHackTools/BillCipher')
	    os.system('mv BillCypher {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def dnsrecon():
	if os.path.exists(f"{CasaDir}/dnsrecon") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/dnsrecon") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> dnsrecon')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python')
	    os.system('git clone https://github.com/darkoperator/dnsrecon')
	    os.system('python -m pip install -r dnsrecon/requirements.txt')
	    os.system('mv dnsrecon {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def zphisher():
	if os.path.exists(f"{CasaDir}/zphisher") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/zphisher") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> zphisher')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php openssh curl')
	    os.system('git clone https://github.com/htr-tech/zphisher')
	    os.system('mv zphisher {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def mrsip():
	if os.path.exists(f"{CasaDir}/Mr.SIP") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Mr.SIP") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Mr.SIP')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('python -m pip install netifaces ipaddress scapy pyfiglet')
	    os.system('git clone https://github.com/meliht/Mr.SIP')
	    os.system('mv Mr.SIP {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def userrecon():
	if os.path.exists(f"{CasaDir}/userrecon_1.0_all.deb") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/userrecon_1.0_all.deb") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> userrecon')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install wget dpkg curl -y')
	    os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/userrecon_1.0_all.deb')
	    os.system('dpkg -i userrecon_1.0_all.deb')
	    os.system('rm userrecon_1.0_all.deb')
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def phoneinfoga():
	if os.path.exists(f"{CasaDir}/PhoneInfoga") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/PhoneInfoga") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> PhoneInfoga')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python git -y')
	    os.system('git clone https://github.com/ExpertAnonymous/PhoneInfoga')
	    os.chdir("PhoneInfoga")
	    os.system("python -m pip install -r requirements.txt")
	    os.chdir("..")
	    os.system('mv PhoneInfoga {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def sitebroker():
	if os.path.exists(f"{CasaDir}/SiteBroker") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/SiteBroker") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> SiteBroker')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python php git -y')
	    os.system('git clone https://github.com/Anon-Exploiter/SiteBroker')
	    os.chdir("SiteBroker")
	    os.system('python -m pip install -r requirements.txt')
	    os.system('python -m pip install html5lib')
	    os.chdir("..")
	    os.system('mv SiteBroker {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def maigret():
	if os.path.exists(f"{CasaDir}/maigret") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/maigret") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> maigret')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install python -y')
	    os.system('python -m pip install maigret')
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;)")
	    print("User: maigret <Nome de Usuário>")
	    print(f"User: maigret -h{b}")
	    backmenu()

def gathetool():
	if os.path.exists(f"{CasaDir}/GatheTOOL") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/GatheTOOL") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> GatheTOOL')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git php python -y')
	    os.system('python -m pip install requests')
	    os.system('git clone https://github.com/AngelSecurityTeam/GatheTOOL')
	    os.system('mv GatheTOOL {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def adbtk():
	if os.path.exists(f"{CasaDir}/ADB-Toolkit") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/ADB-Toolkit") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> ADB-Toolkit')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git -y')
	    os.system('git clone https://github.com/ASHWIN990/ADB-Toolkit')
	    os.system('mv ADB-Toolkit {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def tekdefense():
	if os.path.exists(f"{CasaDir}/TekDefense-Automater") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/TekDefense-Automater") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> TekDefense-Automater')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 -y')
	    os.system('python2 -m pip install requests')
	    os.system('git clone https://github.com/1aN0rmus/TekDefense-Automater')
	    os.system('mv TekDefense-Automater {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def eagleeye():
	if os.path.exists(f"{CasaDir}/EagleEye") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/EagleEye") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> EagleEye')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('python -m pip install termcolor opencv-python selenium face_recognition WeasyPrint requests-html')
	    os.system('git clone https://github.com/ThoughtfulDev/EagleEye')
	    os.system('mv EagleEye {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def eyewitness():
	if os.path.exists(f"{CasaDir}/EyeWitness") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/EyeWitness") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> EyeWitness')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('git clone https://github.com/FortyNorthSecurity/EyeWitness')
	    os.system('mv EyeWitness {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def inspy():
	if os.path.exists(f"{CasaDir}/InSpy") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/InSpy") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> InSpy')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 -y')
	    os.system('python2 -m pip install requests==2.20.1 BeautifulSoup==3.2.1')
	    os.system('git clone https://github.com/leapsecurity/InSpy')
	    os.system('mv InSpy {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def leaked():
	if os.path.exists(f"{CasaDir}/Leaked") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/Leaked") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> Leaked')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python -y')
	    os.system('python -m pip install requests')
	    os.system('git clone https://github.com/GitHackTools/Leaked')
	    os.system('mv Leaked {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()

def fierce():
	if os.path.exists(f"{CasaDir}/fierce") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/fierce") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> fierce')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 -y')
	    os.system('python2 -m pip install dnspython==1.16.0 fierce')
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;)")
	    print(f"User: fierce -h{b}")
	    backmenu()

def gasmask():
	if os.path.exists(f"{CasaDir}/gasmask") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/home'{vd}");timeout(1);
	elif os.path.exists(f"{Dirbin}/gasmask") == True:
	    Installed_banner()
	    print(f"\n{vlh}Essa ferramenta já ser encontra no diretório ->{am}'/bin'{vd}");timeout(1);
	else:
	    install_banner()
	    print(f'{v}\nINSTALANDO --> gasmask')
	    os.system('apt update -y && apt upgrade -y')
	    os.system('apt install git python2 -y')
	    os.system('python2 -m pip install validators python-whois dnspython requests shodan censys')
	    os.system('git clone https://github.com/twelvesec/gasmask')
	    os.system('mv gasmask {}'.format(CasaDir))
	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	    backmenu()
