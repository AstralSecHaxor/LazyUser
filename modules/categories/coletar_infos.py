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
    install_banner()
    print(f'{v}\nINSTALANDO --> D-TECT')
    os.system('apt update -y && apt upgrade -y')
    os.system('apt install python2 git')
    os.system('git clone https://github.com/bibortone/D-Tech')
    os.system('mv D-Tech {}/D-TECT'.format(CasaDir))
    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    backmenu()

def sqlmap():
    install_banner()
    print(f'{v}\nINSTALANDO --> sqlmap')
    os.system('apt update -y && apt upgrade -y')
    os.system('apt install git python2')
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap {}'.format(CasaDir))
    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    backmenu()

def infoga():
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
	install_banner()
	print(f'{v}\nINSTALANDO --> ReconDog')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/ReconDog')
	os.system('mv ReconDog {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def androZenmap():
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
	install_banner()
	print(f'{v}\nINSTALANDO --> AstraNmap')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def mapeye():
	print(f'{v}\nINSTALANDO --> MapEye')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/bhikandeshmukh/MapEye')
	os.system('mv MapEye {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def easyMap():
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
	print(f'{v}\nINSTALANDO --> BlackBox')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git && python2 -m pip install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def xd3v():
	install_banner()
	print(f'{v}\nINSTALANDO --> XD3v')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install curl')
	os.system('curl -k -O https:/MapEye/gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	os.system('mv xd3v.sh {0}/../usr/bin/xd3v && chmod +x {0}/../usr/bin/xd3v'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	print("User: 'xd3v' para começar")
	backmenu()

def crips():
	install_banner()
	print(f'{v}\nINSTALANDO --> Crips')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 openssl curl libcurl wget")
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips {}".format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def sir():
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
	install_banner()
	print(f'{v}\nINSTALANDO --> EvilURL')
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 python3")
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL {}".format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def striker():
	install_banner()
	print(f'{v}\nINSTALANDO --> Striker')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('git clone https://github.com/s0md3v/Striker')
	os.system('mv Striker {}'.format(CasaDir))
	os.system('cd {}/Striker && python2 -m pip install -r requirements.txt'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def xshell():
	install_banner()
	print(f'{v}\nINSTALANDO --> Xshell')
	os.system("apt update && apt upgrade")
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell {}".format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def owscan():
	print(f'{v}\nINSTALANDO --> OWScan')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/OWScan')
	os.system('mv OWScan {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def osif():
	print(f'{v}\nINSTALANDO --> OSIF')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/CiKu370/OSIF')
	os.system('mv OSIF {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def devploit():
	print(f'{v}\nINSTALANDO --> Devploit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python2 git && python2 -m pip install urllib2')
	os.system('git clone https://github.com/joker25000/Devploit')
	os.system('mv Devploit {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def namechk():
	print(f'{v}\nINSTALANDO --> Namechk')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git')
	os.system('git clone https://github.com/HA71/Namechk')
	os.system('mv Namechk {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def auxile():
	print(f'{v}\nINSTALANDO --> AUXILE')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	os.system('git clone https://github.com/CiKu370/AUXILE')
	os.system('mv AUXILE {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def inther():
	print(f'{v}\nINSTALANDO --> inther')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git ruby')
	os.system('git clone https://github.com/Gameye98/inther')
	os.system('mv inther {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def ginf():
	print(f'{v}\nINSTALANDO --> GINF')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/GINF')
	os.system('mv GINF {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def gpstr():
	print(f'{v}\nINSTALANDO --> GPS Tracking')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install php git')
	os.system('git clone https://github.com/indosecid/gps_tracking')
	os.system('mv gps_tracking {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def asu():
	print(f'{v}\nINSTALANDO --> ASU')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 php')
	os.system('python2 -m pip install requests bs4 mechanize')
	os.system('git clone https://github.com/LOoLzeC/ASU')
	os.system('mv ASU {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def fim():
	print(f'{v}\nINSTALANDO --> fim')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python && python -m pip install requests bs4')
	os.system('git clone https://github.com/karjok/fim')
	os.system('mv fim {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def maxsubdofinder():
	print(f'{v}\nINSTALANDO --> MaxSubdoFinder')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/maxteroit/MaxSubdoFinder')
	os.system('mv MaxSubdoFinder {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def pwnedOrNot():
	print(f'{v}\nINSTALANDO --> pwnedOrNot')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
	os.system('mv pwnedOrNot {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def maclook():
	print(f'{v}\nINSTALANDO --> Mac-Lookup')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/T4P4N/Mac-Lookup')
	os.system('mv Mac-Lookup {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def billcypher():
	print(f'{v}\nINSTALANDO --> BillCypher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('python -m pip install argparse dnspython requests urllib3 colorama')
	os.system('git clone https://github.com/GitHackTools/BillCipher')
	os.system('mv BillCypher {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def dnsrecon():
	print(f'{v}\nINSTALANDO --> dnsrecon')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python')
	os.system('git clone https://github.com/darkoperator/dnsrecon')
	os.system('python -m pip install -r dnsrecon/requirements.txt')
	os.system('mv dnsrecon {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def zphisher():
	print(f'{v}\nINSTALANDO --> zphisher')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php openssh curl')
	os.system('git clone https://github.com/htr-tech/zphisher')
	os.system('mv zphisher {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def mrsip():
	print(f'{v}\nINSTALANDO --> Mr.SIP')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install netifaces ipaddress scapy pyfiglet')
	os.system('git clone https://github.com/meliht/Mr.SIP')
	os.system('mv Mr.SIP {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def userrecon():
	print(f'{v}\nINSTALANDO --> userrecon')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install wget dpkg curl -y')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/userrecon_1.0_all.deb')
	os.system('dpkg -i userrecon_1.0_all.deb')
	os.system('rm userrecon_1.0_all.deb')
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def phoneinfoga():
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
	print(f'{v}\nINSTALANDO --> maigret')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install python -y')
	os.system('python -m pip install maigret')
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;)")
	print("User: maigret <Nome de Usuário>")
	print(f"User: maigret -h{b}")
	backmenu()

def gathetool():
	print(f'{v}\nINSTALANDO --> GatheTOOL')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/AngelSecurityTeam/GatheTOOL')
	os.system('mv GatheTOOL {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def adbtk():
	print(f'{v}\nINSTALANDO --> ADB-Toolkit')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git -y')
	os.system('git clone https://github.com/ASHWIN990/ADB-Toolkit')
	os.system('mv ADB-Toolkit {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def tekdefense():
	print(f'{v}\nINSTALANDO --> TekDefense-Automater')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/1aN0rmus/TekDefense-Automater')
	os.system('mv TekDefense-Automater {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def eagleeye():
	print(f'{v}\nINSTALANDO --> EagleEye')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install termcolor opencv-python selenium face_recognition WeasyPrint requests-html')
	os.system('git clone https://github.com/ThoughtfulDev/EagleEye')
	os.system('mv EagleEye {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def eyewitness():
	print(f'{v}\nINSTALANDO --> EyeWitness')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('git clone https://github.com/FortyNorthSecurity/EyeWitness')
	os.system('mv EyeWitness {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def inspy():
	print(f'{v}\nINSTALANDO --> InSpy')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests==2.20.1 BeautifulSoup==3.2.1')
	os.system('git clone https://github.com/leapsecurity/InSpy')
	os.system('mv InSpy {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def leaked():
	print(f'{v}\nINSTALANDO --> Leaked')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/GitHackTools/Leaked')
	os.system('mv Leaked {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

def fierce():
	print(f'{v}\nINSTALANDO --> fierce')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install dnspython==1.16.0 fierce')
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;)")
	print(f"User: fierce -h{b}")
	backmenu()

def gasmask():
	print(f'{v}\nINSTALANDO --> gasmask')
	os.system('apt update -y && apt upgrade -y')
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install validators python-whois dnspython requests shodan censys')
	os.system('git clone https://github.com/twelvesec/gasmask')
	os.system('mv gasmask {}'.format(CasaDir))
	print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
	backmenu()

