#!/bin/bash
#  _____________________________________________________
# +=[ Version 0.2 - beta                               
# +=[ BY: AstralSecHaxor From Brazil                   
# +=[ YouTube: https://youtube.com/@AstralSec_Haxor    
# +=[ Github: https://github.com/AstralSecHaxor/LazyUser
#  —————————————————————————————————————————————————————

# SCRIPT DE INSTALAÇÕES DE DEPENDÊNCIAS DO TOOL

vermelho='\033[0;31m'    # Vermelho
verde='\033[0;32m'       # Verde
amarelo='\033[0;33m'     # Amarelo
azul='\033[0;34m'        # Azul
magenta='\033[0;35m'     # Magenta
ciano='\033[0;36m'       # Ciano
branco='\033[0;37m'      # Branco
reset='\033[0m'          # Reset para a cor padrão
clear
echo " "
echo -e "${ciano} __         ______     ______     __  __             "
echo -e "/\ \       /\  __ \   /\___  \   /\ \_\ \                    "
echo -e "\ \ \____  \ \  __ \  \/_/  /__  \ \____ \     ${ciano}Version ${azul}0.2${ciano}   "
echo -e " \ \_____\  \ \_\ \_\   /\_____\  \/\_____\                  "
echo -e "  \/_____/   \/_/\/_/   \/_____/   \/_____/                  "
echo -e "                 __  __     ______     ______     ______     "
echo -e "                /\ \/\ \   /\  ___\   /\  ___\   /\  == \    "
echo -e "                \ \ \_\ \  \ \___  \  \ \  __\   \ \  __<    "
echo -e "                 \ \_____\  \/\_____\  \ \_____\  \ \_\ \_\  "
echo -e "                  \/_____/   \/_____/   \/_____/   \/_/ /_/  "
echo -e "                                                             "
echo -e "         ${azul}+${magenta}-- -${azul}+${amarelo}=${branco}[ By: AstralSec${vermelho}Haxor${reset} from Brazil ]${amarelo}=${magenta}- --${azul}+${reset}"


# Função para verificar se um comando foi executado com sucesso
function verificar_sucesso {
  if [ $? -eq 0 ]; then
    echo -e "\n[${verde} ✔ ${reset}] ${ciano}instalação concluída com sucesso.${reset}"
  else
    echo -e "\n[${vermelho} !! ${reset}]${vermelho} A instalação do Tool falhou devido a um erro durante o processo.${reset}"
    echo -e "\n[${vermelho} !! ${reset}]${vermelho} Lamento, mas não foi possível continuar :(${reset}"
    exit 1
  fi
}

# Atualiza a lista de pacotes e faz o upgrade
echo -e "\n\n${reset}[${magenta} ... ${reset}] ${verde}Atualizando lista de pacotes e fazendo upgrade...${reset}"
apt-get update -y && apt-get upgrade -y
echo -e "\n${reset}[${verde} ✔ ${reset}] ${ciano}Atualizando concluída. ${reset}"
# Verificando se a atualização foi bem-sucedida

# Lista de pacotes
dependencies=("git" "python3" "pip")

for package in "${dependencies[@]}"; do
    ## Checando se o pacote já foi instalado
    if dpkg -l | grep -q "^ii.*$package "; then
        echo -e "\n[${verde} ✔ ${reset}]${amarelo} $package ${verde}está instalado.${reset}"
    else
        ## Fazendo a instalação do pacote
        echo -e "\n[${magenta} ... ${reset}] ${verde}Instalando -->${amarelo} $package ... ${reset}"
        # Comando de instalação dos pacotes
        apt-get install -y "$package"
        # Verifique se a instalação foi bem-sucedida
        verificar_sucesso
    fi
done

# Instalação da biblioteca Pillow
echo -e "\n[${magenta} ... ${reset}] ${verde}Instalando  biblioteca --> ${amarelo}Pillow...${reset}"
apt install python make wget termux-exec clang libjpeg-turbo freetype -y
env INCLUDE="$PREFIX/include" LDFLAGS=" -lm" pip install Pillow

verificar_sucesso



# instalação de libs
dependencies=("python-telegram-bot" "requests")
for package in "${dependencies[@]}"; do
    ## Checando se o pacote já foi instalado
    if command -v "$package" >/dev/null 2>&1; then
        echo -e "\n[${verde} ✔ ${reset}]${amarelo} $package ${verde}está instalado.${reset}"
    else
        ## Fazendo a instalação do pacote usando pip
        echo -e "\n[${magenta} ... ${reset}] ${verde}Instalando biblioteca -->${amarelo} $package ... ${reset}"
        # Comando de instalação dos pacotes usando pip
        pip install "$package"
        # Verifique se a instalação foi bem-sucedida
        verificar_sucesso
    fi
done
# Clona o repositório LazyUser e executa install.py
echo -e "\n[${magenta} ... ${reset}]${verde} Clonando o repositório ${amarelo}'LazyUser'${verde} ${verde}e executando ${amarelo}'setup.py'${verde} ...${reset}"
git clone https://github.com/AstralSecHaxor/LazyUser
verificar_sucesso
echo -e " "
python3 LazyUser/setup.py
rm -rf LazyUser
exit

###wget -O script.sh https://raw.githubusercontent.com/usuario/repositorio/master/script.sh && chmod +x script.sh && ./script.sh
