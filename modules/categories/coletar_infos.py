"""
BANCO DE DADOS DA CATEGORIA: coletar de informações
TODAS AS FERRAMENTAS RELACIONADAS COM ESSA CATEGORIA ESTARÃO AQUI.
"""
import os
from modules.logos import *
from os.path import exists

# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" #vermelho 
bra = "\33[1;37m" # branco
az = '\033[34m' # Azul
ma = '\033[35m' #Magento
am = '\033[33m' #Amarelo 


# Obtém o caminho da pasta home do usuário atual
homme = os.path.expanduser("~")
# Lista de diretórios a serem verificados pela  presença de alguma ferramenta instalada via apt
directories_to_check = ["/usr/lib", "/lib", "/usr/bin", "/bin", "/usr/sbin", "/sbin", "/usr/share"]
for bIn in directories_to_check:
    def nmap():
        if os.path.exists(f"{homme}/nmap") == True:
            Installed_banner()
            print(f"O {am}Nmap{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
        elif os.path.exists(f"{bIn}/nmap") == True:
            Installed_banner()
            print(f"O {am}Nmap{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
        else:
    	    install_banner()
    	    print(f'{v}INSTALANDO --> Nmap')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install nmap')
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	
    def red_hawk():
        if os.path.exists(f"{homme}/RED_HAWK") == True:
            Installed_banner()
            print(f"O {am}RED_HAWK{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
        elif os.path.exists(f"{bIn}/RED_HAWK") == True:
            Installed_banner()
            print(f"O {am}RED_HAWK{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
        else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> RED HAWK')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git php')
    	    os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
    	    os.system('mv RED_HAWK {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    def dtect():
    	if os.path.exists(f"{homme}/D-TECT") == True:
    	    Installed_banner()
    	    print(f"O {am}D-TECT{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/D-TECT") == True:
    	    Installed_banner()
    	    print(f"O {am}D-TECT{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> D-TECT')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install python2 git')
    	    os.system('git clone https://github.com/bibortone/D-Tech')
    	    os.system('mv D-Tech {}/D-TECT'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    
    def sqlmap():
    	if os.path.exists(f"{homme}/sqlmap") == True:
    	    Installed_banner()
    	    print(f"O {am}SQLMap{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/sqlmap") == True:
    	    Installed_banner()
    	    print(f"O {am}SQLMap{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> sqlmap')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python2')
    	    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    	    os.system('mv sqlmap {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    
    def reconDog():
    	if os.path.exists(f"{homme}/ReconDog") == True:
    	    Installed_banner()
    	    print(f"O {am}ReconDog{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/ReconDog") == True:
    	    Installed_banner()
    	    print(f"O {am}ReconDog{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> ReconDog')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install python2 git -y')
    	    os.system('git clone https://github.com/s0md3v/ReconDog')
    	    os.system('mv ReconDog {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    def androZenmap():
    	if os.path.exists(f"{homme}/AndroZenmap") == True:
    	    Installed_banner()
    	    print(f"O {am}AndroZenmap{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/AndroZenmap") == True:
    	    Installed_banner()
    	    print(f"O {am}AndroZenmap{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> AndroZenmap')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install nmap curl')
    	    os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
    	    os.system('mkdir {}/AndroZenmap'.format(homme))
    	    os.system('mv androzenmap.sh {}/AndroZenmap'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def sqlmate():
    	if os.path.exists(f"{homme}/sqlmate") == True:
    	    Installed_banner()
    	    print(f"O {am}SQLMate{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/sqlmate") == True:
    	    Installed_banner()
    	    print(f"O {am}SQLMate{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> sqlmate')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install python2 git')
    	    os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
    	    os.system('git clone https://github.com/s0md3v/sqlmate')
    	    os.system('mv sqlmate {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def astraNmap():
    	if os.path.exists(f"{homme}/AstraNmap") == True:
    	    Installed_banner()
    	    print(f"O {am}AstraNmap{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/AstraNmap") == True:
    	    Installed_banner()
    	    print(f"O  {am}AstraNmap{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> AstraNmap')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git nmap')
    	    os.system('git clone https://github.com/Gameye98/AstraNmap')
    	    os.system('mv AstraNmap {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def mapeye():
    	if os.path.exists(f"{homme}/MapEye") == True:
    	    Installed_banner()
    	    print(f"O {am}MapEye{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/MapEye") == True:
    	    Installed_banner()
    	    print(f"O {am}MapEye{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> MapEye')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git php python -y')
    	    os.system('python -m pip install requests')
    	    os.system('git clone https://github.com/bhikandeshmukh/MapEye')
    	    os.system('mv MapEye {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def easyMap():
    	if os.path.exists(f"{homme}/Easymap") == True:
    	    Installed_banner()
    	    print(f"O {am}EasyMap{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/Easymap") == True:
    	    Installed_banner()
    	    print(f"O {am}EasyMap{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Easymap')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install php -y')
    	    os.system('apt install git -y')
    	    os.system('git clone https://github.com/Cvar1984/Easymap')
    	    os.system('mv Easymap {}'.format(homme))
    	    os.system('cd {}/Easymap && sh install.sh'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def crips():
    	if os.path.exists(f"{homme}/Crips") == True:
    	    Installed_banner()
    	    print(f"O {am}Crips{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/Crips") == True:
    	    Installed_banner()
    	    print(f"O {am}Crips{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Crips')
    	    os.system("apt update && apt upgrade")
    	    os.system("apt install git python2 openssl curl libcurl wget")
    	    os.system("git clone https://github.com/Manisso/Crips")
    	    os.system("mv Crips {}".format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def evilURL():
    	if os.path.exists(f"{homme}/EvilURL") == True:
    	    Installed_banner()
    	    print(f"O {am}EvilURL{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/EvilURL") == True:
    	    Installed_banner()
    	    print(f"O {am}EvilURL{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> EvilURL')
    	    os.system("apt update && apt upgrade")
    	    os.system("apt install git python2 python3")
    	    os.system("git clone https://github.com/UndeadSec/EvilURL")
    	    os.system("pip install python-nmap python-whois")
    	    os.system("mv EvilURL {}".format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def striker():
    	if os.path.exists(f"{homme}/Striker") == True:
    	    Installed_banner()
    	    print(f"O {am}Striker{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/Striker") == True:
    	    Installed_banner()
    	    print(f"O {am}Striker{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Striker')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python2')
    	    os.system('git clone https://github.com/s0md3v/Striker')
    	    os.system('mv Striker {}'.format(homme))
    	    os.system('cd /Striker && python2 -m pip install -r requirements.txt'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def xshell():
    	if os.path.exists(f"{homme}/Xshell") == True:
    	    Installed_banner()
    	    print(f"O {am}Xshell{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/Xshell") == True:
    	    Installed_banner()
    	    print(f"O {am}Xshell{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Xshell')
    	    os.system("apt update && apt upgrade")
    	    os.system("apt install lynx python2 figlet ruby php nano w3m")
    	    os.system("git clone https://github.com/Ubaii/Xshell")
    	    os.system("mv Xshell {}".format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def owscan():
    	if os.path.exists(f"{homme}/OWScan") == True:
    	    Installed_banner()
    	    print(f"O {am}OWScan{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/OWScan") == True:
    	    Installed_banner()
    	    print(f"O {am}OWScan{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> OWScan')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git php')
    	    os.system('git clone https://github.com/Gameye98/OWScan')
    	    os.system('mv OWScan {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def osif():
    	if os.path.exists(f"{homme}/OSIF") == True:
    	    Installed_banner()
    	    print(f"O {am}OSIF{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/OSIF") == True:
    	    Installed_banner()
    	    print(f"O {am}OSIF{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> OSIF')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python2')
    	    os.system('python2 -m pip install requests')
    	    os.system('git clone https://github.com/CiKu370/OSIF')
    	    os.system('mv OSIF {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def namechk():
    	if os.path.exists(f"{homme}/Namechk") == True:
    	    Installed_banner()
    	    print(f"O {am}Namechk{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/Namechk") == True:
    	    Installed_banner()
    	    print(f"O {am}Namechk{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Namechk')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git')
    	    os.system('git clone https://github.com/HA71/Namechk')
    	    os.system('mv Namechk {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def auxile():
    	if os.path.exists(f"{homme}/AUXILE") == True:
    	    Installed_banner()
    	    print(f"O {am}AUXILE{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/AUXILE") == True:
    	    Installed_banner()
    	    print(f"O {am}AUXILE{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> AUXILE')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
    	    os.system('git clone https://github.com/CiKu370/AUXILE')
    	    os.system('mv AUXILE {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def inther():
    	if os.path.exists(f"{homme}/inther") == True:
    	    Installed_banner()
    	    print(f"O {am}Inther{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/inther") == True:
    	    Installed_banner()
    	    print(f"O {am}Inther{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> inther')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git ruby')
    	    os.system('git clone https://github.com/Gameye98/inther')
    	    os.system('mv inther {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    def ginf():
    	if os.path.exists(f"{homme}/GINF") == True:
    	    Installed_banner()
    	    print(f"O {am}GINF{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/GINF") == True:
    	    Installed_banner()
    	    print(f"O {am}GINF{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> GINF')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git php')
    	    os.system('git clone https://github.com/Gameye98/GINF')
    	    os.system('mv GINF {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def gpstr():
    	if os.path.exists(f"{homme}/gps_tracking") == True:
    	    Installed_banner()
    	    print(f"O {am}GPS_Tracking{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/gps_tracking") == True:
    	    Installed_banner()
    	    print(f"O {am}GPS_Tracking{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> GPS Tracking')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install php git')
    	    os.system('git clone https://github.com/indosecid/gps_tracking')
    	    os.system('mv gps_tracking {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def asu():
    	if os.path.exists(f"{homme}/ASU") == True:
    	    Installed_banner()
    	    print(f"O {am}ASU{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/ASU") == True:
    	    Installed_banner()
    	    print(f"O {am}ASU{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> ASU')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python2 php')
    	    os.system('python2 -m pip install requests bs4 mechanize')
    	    os.system('git clone https://github.com/LOoLzeC/ASU')
    	    os.system('mv ASU {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def fim():
    	if os.path.exists(f"{homme}/fim") == True:
    	    Installed_banner()
    	    print(f"O {am}Fim{ma} já está presente no diretório {vlh}(; {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/fim") == True:
    	    Installed_banner()
    	    print(f"O {am}Fim{ma} já está presente no diretório {vlh}(; {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> fim')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python && python -m pip install requests bs4')
    	    os.system('git clone https://github.com/karjok/fim')
    	    os.system('mv fim {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    #################parei
    def pwnedOrNot():
    	if os.path.exists(f"{homme}/pwnedOrNot") == True:
    	    Installed_banner()
    	    print(f"O {am}PwnedOrNot{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/pwnedOrNot") == True:
    	    Installed_banner()
    	    print(f"O {am}PwnedOrNot{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> pwnedOrNot')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python')
    	    os.system('python -m pip install requests')
    	    os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
    	    os.system('mv pwnedOrNot {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def dnsrecon():
    	if os.path.exists(f"{homme}/dnsrecon") == True:
    	    Installed_banner()
    	    print(f"O {am}DNSRecon{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/dnsrecon") == True:
    	    Installed_banner()
    	    print(f"O {am}DNSRecon{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> dnsrecon')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python')
    	    os.system('apt install pip')
    	    os.system('pip install dnsrecon')
    	    os.system('mv dnsrecon {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def zphisher():
    	if os.path.exists(f"{homme}/zphisher") == True:
    	    Installed_banner()
    	    print(f"O {am}Zphisher{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/zphisher") == True:
    	    Installed_banner()
    	    print(f"O {am}Zphisher{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> zphisher')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git php openssh curl')
    	    os.system('git clone https://github.com/htr-tech/zphisher')
    	    os.system('mv zphisher {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    	    
    def mrsip():
    	if os.path.exists(f"{homme}/Mr.SIP") == True:
    	    Installed_banner()
    	    print(f"O {am}MR.SIP{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/Mr.SIP") == True:
    	    Installed_banner()
    	    print(f"O {am}MR.SIP{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Mr.SIP')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python -y')
    	    os.system('python -m pip install netifaces ipaddress scapy pyfiglet')
    	    os.system('git clone https://github.com/meliht/Mr.SIP')
    	    os.system('mv Mr.SIP {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def userrecon():
    	if os.path.exists(f"{homme}/userrecon_1.0_all.deb") == True:
    	    Installed_banner()
    	    print(f"O {am}UserRecon{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/userrecon_1.0_all.deb") == True:
    	    Installed_banner()
    	    print(f"O {am}UserRecon{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> userrecon')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install wget dpkg curl -y')
    	    os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/userrecon_1.0_all.deb')
    	    os.system('dpkg -i userrecon_1.0_all.deb')
    	    os.system('rm userrecon_1.0_all.deb')
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def phoneinfoga():
    	if os.path.exists(f"{homme}/PhoneInfoga") == True:
    	    Installed_banner()
    	    print(f"O {am}PhoneInfoga{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/PhoneInfoga") == True:
    	    Installed_banner()
    	    print(f"O {am}PhoneInfoga{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> PhoneInfoga')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install python git -y')
    	    os.system('git clone https://github.com/ExpertAnonymous/PhoneInfoga')
    	    os.system('mv PhoneInfoga {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def sitebroker():
    	if os.path.exists(f"{homme}/SiteBroker") == True:
    	    Installed_banner()
    	    print(f"O {am}SiteBroker{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/SiteBroker") == True:
    	    Installed_banner()
    	    print(f"O {am}SiteBroker{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
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
    	    os.system('mv SiteBroker {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def gathetool():
    	if os.path.exists(f"{homme}/GatheTOOL") == True:
    	    Installed_banner()
    	    print(f"O {am}GatheTOOL{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/GatheTOOL") == True:
    	    Installed_banner()
    	    print(f"O {am}GatheTOOL{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> GatheTOOL')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git php python -y')
    	    os.system('python -m pip install requests')
    	    os.system('git clone https://github.com/AngelSecurityTeam/GatheTOOL')
    	    os.system('mv GatheTOOL {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def adbtk():
    	if os.path.exists(f"{homme}/ADB-Toolkit") == True:
    	    Installed_banner()
    	    print(f"O {am}ADB-Toolkit{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/ADB-Toolkit") == True:
    	    Installed_banner()
    	    print(f"O {am}ADB-Toolkit{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> ADB-Toolkit')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git -y')
    	    os.system('git clone https://github.com/ASHWIN990/ADB-Toolkit')
    	    os.system('mv ADB-Toolkit {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def tekdefense():
    	if os.path.exists(f"{homme}/TekDefense-Automater") == True:
    	    Installed_banner()
    	    print(f"O {am}TekDefense-Automater{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/TekDefense-Automater") == True:
    	    Installed_banner()
    	    print(f"O {am}TekDefense-Automater{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> TekDefense-Automater')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python2 -y')
    	    os.system('python2 -m pip install requests')
    	    os.system('git clone https://github.com/1aN0rmus/TekDefense-Automater')
    	    os.system('mv TekDefense-Automater {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def eagleeye():
    	if os.path.exists(f"{homme}/EagleEye") == True:
    	    Installed_banner()
    	    print(f"O {am}EagleEye{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/EagleEye") == True:
    	    Installed_banner()
    	    print(f"O {am}EagleEye{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> EagleEye')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python -y')
    	    os.system('apt install pip -y')
    	    os.system('pip install termcolor')
    	    os.system('pip install selenium')
    	    os.system('pip install requests_html')
    	    os.system('pip install opencv-python')
    	    os.system('git clone https://github.com/ThoughtfulDev/EagleEye')
    	    os.system('mv EagleEye {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def eyewitness():
    	if os.path.exists(f"{homme}/EyeWitness") == True:
    	    Installed_banner()
    	    print(f"O {am}EyeWitness{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/EyeWitness") == True:
    	    Installed_banner()
    	    print(f"O {am}EyeWitness{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> EyeWitness')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python -y')
    	    os.system('git clone https://github.com/FortyNorthSecurity/EyeWitness')
    	    os.system('mv EyeWitness {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def inspy():
    	if os.path.exists(f"{homme}/InSpy") == True:
    	    Installed_banner()
    	    print(f"O {am}InSpy{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/InSpy") == True:
    	    Installed_banner()
    	    print(f"O {am}InSpy{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> InSpy')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python2 -y')
    	    os.system('python2 -m pip install requests==2.20.1 BeautifulSoup==3.2.1')
    	    os.system('git clone https://github.com/leapsecurity/InSpy')
    	    os.system('mv InSpy {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def fierce():
    	if os.path.exists(f"{homme}/fierce") == True:
    	    Installed_banner()
    	    print(f"O {am}Fierce{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/fierce") == True:
    	    Installed_banner()
    	    print(f"O {am}Fierce{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> fierce')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python -y')
    	    os.system('pip install dnspython==1.16.0 fierce')
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;)")
    	    print(f"User: fierce -h{b}")
    	    
    
    def gasmask():
    	if os.path.exists(f"{homme}/gasmask") == True:
    	    Installed_banner()
    	    print(f"O {am}Gasmask{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/gasmask") == True:
    	    Installed_banner()
    	    print(f"O {am}Gasmask{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> gasmask')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python2 -y')
    	    os.system('python2 -m pip install validators python-whois dnspython requests shodan censys')
    	    os.system('git clone https://github.com/twelvesec/gasmask')
    	    os.system('mv gasmask {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    	    
    def sherlock():
    	if os.path.exists(f"{homme}/sherlock") == True:
    	    Installed_banner()
    	    print(f"O {am}Shelock{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/sherlock/") == True:
    	    Installed_banner()
    	    print(f"O {am}Sherlock{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> sherlock')
    	    os.system("apt update -y && apt upgrade -y")
    	    os.system("apt install git -y")
    	    os.system("apt install python -y")
    	    os.system("git clone https://github.com/sherlock-project/sherlock.git")
    	    os.system("mv sherlock {}".format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    