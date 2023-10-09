"""
BANCO DE DADOS DA CATEGORIA: Análise de Vulnerabilidades 
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
    def sqliv():
    	if os.path.exists(f"{homme}/sqliv") == True:
    	    Installed_banner()
    	    print(f"O {am}SQLiv{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/sqliv") == True:
    	    Installed_banner()
    	    print(f"O {am}SQLiv{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> SQLiv')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install python2 git')
    	    os.system('git clone https://github.com/the-robot/sqliv')
    	    os.system('mv sqliv {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    
    def sqlscan():
    	if os.path.exists(f"{homme}/sqlscan") == True:
    	    Installed_banner()
    	    print(f"O {am}SQLscan{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/sqlscan") == True:
    	    Installed_banner()
    	    print(f"O {am}SQLscan{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> sqlscan')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git php')
    	    os.system('git clone http://www.github.com/Cvar1984/sqlscan')
    	    os.system('mv sqlscan {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def wordpreSScan():
    	if os.path.exists(f"{homme}/Wordpresscan") == True:
    	    Installed_banner()
    	    print(f"O {am}Wordpresscan{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/Wordpresscan") == True:
    	    Installed_banner()
    	    print(f"O {am}Wordpresscan{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Wordpresscan')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
    	    os.system('mv Wordpresscan {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    	
    def wpscan():
    	if os.path.exists(f"{homme}/wpscan") == True:
    	    Installed_banner()
    	    print(f"O {am}WPScan{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/wpscan") == True:
    	    Installed_banner()
    	    print(f"O {am}WPScan{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> WPScan')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git ruby curl')
    	    os.system('git clone https://github.com/wpscanteam/wpscan')
    	    os.system('mv wpscan {0} && cd {0}/wpscan'.format(homme))
    	    os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def wordpresscan():
    	if os.path.exists(f"{homme}/termux-wordpresscan") == True:
    	    Installed_banner()
    	    print(f"O {am}Termux-Wordpresscan{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/termux-wordpresscan") == True:
    	    Installed_banner()
    	    print(f"O {am}Termux-Wordpresscan{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Termux-Wordpresscan')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install nmap figlet git')
    	    os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
    	    os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
    	    os.system('mv termux-wordpresscan {}'.format(homme))
    	    print(f"{vd}\nUser: wordpresscan para começar")
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def tmscanner():
    	if os.path.exists(f"{homme}/TM-scanner") == True:
    	    Installed_banner()
    	    print(f"O {am}TM-scanner{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/TM-scanner") == True:
    	    Installed_banner()
    	    print(f"O {am}TM-scanner{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> TM-scanner')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install python python2 nmap git -y')
    	    os.system('python -m pip install colorama requests')
    	    os.system('python2 -m pip install colorama requests')
    	    os.system('git clone https://github.com/TechnicalMujeeb/TM-scanner')
    	    os.system('mv TM-scanner {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def rang3r():
    	if os.path.exists(f"{homme}/rang3r") == True:
    	    Installed_banner()
    	    print(f"O {am}Rang3r{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/rang3r") == True:
    	    Installed_banner()
    	    print(f"O {am}Rang3r{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Rang3r')
    	    os.system("apt update && apt upgrade")
    	    os.system("apt install git python")
    	    os.system("git clone https://github.com/floriankunushevci/rang3r")
    	    os.system("mv rang3r {}".format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def routersploit():
    	if os.path.exists(f"{homme}/routersploit") == True:
    	    Installed_banner()
    	    print(f"O {am}RouterSploit{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/routersploit") == True:
    	    Installed_banner()
    	    print(f"O {am}RouterSploit{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Routersploit')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install python2 git')
    	    os.system('python2 -m pip install requests')
    	    os.system('git clone https://github.com/threat9/routersploit')
    	    os.system('mv routersploit {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def sh33ll():
    	if os.path.exists(f"{homme}/SH33LL") == True:
    	    Installed_banner()
    	    print(f"O {am}SH33LL{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/SH33LL") == True:
    	    Installed_banner()
    	    print(f"O {am}SH33LL{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> SH33LL')
    	    os.system("apt update && apt upgrade")
    	    os.system("apt install git python2")
    	    os.system("git clone https://github.com/LOoLzeC/SH33LL")
    	    os.system("mv SH33LL {}".format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def xplsearch():
    	if os.path.exists(f"{homme}/XPL-SEARCH") == True:
    	    Installed_banner()
    	    print(f"O {am}XPL-SEARCH{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/XPL-SEARCH") == True:
    	    Installed_banner()
    	    print(f"O {am}XPL-SEARCH{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> XPL-SEARCH')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git php -y')
    	    os.system('git clone https://github.com/r00tmars/XPL-SEARCH')
    	    os.system('mv XPL-SEARCH {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def androbugs():
    	if os.path.exists(f"{homme}/AndroBugs_Framework") == True:
    	    Installed_banner()
    	    print(f"O {am}AndroBugs_Framework{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/AndroBugs_Framework") == True:
    	    Installed_banner()
    	    print(f"O {am}AndroBugs_Framework{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> AndroBugs_Framework')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python2 -y')
    	    os.system('python2 -m pip install pymongo')
    	    os.system('git clone https://github.com/AndroBugs/AndroBugs_Framework')
    	    os.system('mv AndroBugs_Framework {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def clickjacking():
    	if os.path.exists(f"{homme}/Clickjacking-Tester") == True:
    	    Installed_banner()
    	    print(f"O {am}Clickjacking-Tester{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/Clickjacking-Tester") == True:
    	    Installed_banner()
    	    print(f"O {am}Clickjacking-Tester{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Clickjacking-Tester')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python -y')
    	    os.system('git clone https://github.com/D4Vinci/Clickjacking-Tester')
    	    os.system('mv Clickjacking-Tester {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
    
    def sn1per():
    	if os.path.exists(f"{homme}/Sn1per") == True:
    	    Installed_banner()
    	    print(f"O {am}Sn1per{ma} já está presente no diretório {am}{homme}{ma}");timeout(1)
    	elif os.path.exists(f"{bIn}/Sn1per") == True:
    	    Installed_banner()
    	    print(f"O {am}Sn1per{ma} já está presente no diretório {am}{bIn}{ma}");timeout(1)
    	else:
    	    install_banner()
    	    print(f'{v}\nINSTALANDO --> Sn1per')
    	    os.system('apt update -y && apt upgrade -y')
    	    os.system('apt install git python -y')
    	    os.system('git clone https://github.com/1N3/Sn1per')
    	    os.chdir("Sn1per")
    	    os.chdir("..")
    	    os.system('mv Sn1per {}'.format(homme))
    	    print(f"{v}\nINSTALAÇÃO CONCLUIDA ;) {b}")
    	    
