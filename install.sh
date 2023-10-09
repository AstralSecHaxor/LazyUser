#!/bin/bash
# SCRIPT DE INSTALAÇÕES DE DEPENDÊNCIAS DO TOOL
# Defina códigos de escape ANSI para cores
vermelho='\033[0;31m' # Vermelho
verde='\033[0;32m'   # Verde
reset='\033[0m'       # Reset para a cor padrão
amarelo='\033[33m'   # Amarelo

# Função para verificar se um comando foi executado com sucesso
function verificar_sucesso {
  if [ $? -eq 0 ]; then
    echo -e "\n${reset}[${verde}*${reset}]${verde} Comando executado com sucesso.${reset}"
  else
    echo -e "\n${reset}[${vermelho}!${reset}]${vermelho} Falha na execução do comando.${reset}"
    echo -e "\n${reset}[${vermelho}!${reset}]${vermelho} Lamento, mas não foi possível continuar :(${reset}"
    exit 1
  fi
}

# Atualiza a lista de pacotes e faz o upgrade
echo -e "\n${reset}[${verde}*${reset}]${verde} Atualizando lista de pacotes e fazendo upgrade...${reset}"
apt-get update -y && apt-get upgrade -y

# Verificando se a atualização foi bem-sucedida
verificar_sucesso

# Lista de pacotes
dependencies=("proot" "git" "python3")

for package in "${dependencies[@]}"; do
    ## Checando se o pacote já foi instalado
    if dpkg -l | grep -q "^ii.*$package "; then
        echo -e "\n${reset}[${verde}*${reset}]${amarelo} $package está instalado.${reset}"
    else    ## Fazendo a instalação do pacote
        echo -e "\n${reset}[${verde}*${reset}] ${verde}Instalando --> $package...${reset}"
        # Comando de instalação dos pacotes
        apt-get install -y "$package"

        # Verifique se a instalação foi bem-sucedida
        verificar_sucesso
    fi
done

# Clona o repositório LazyUser e executa install.py
echo -e "\n${reset}[${verde}*${reset}]${verde} Clonando o repositório 'LazyUser' e executando 'install.py'...${reset}"
git clone https://github.com/AstralSecHaxor/LazyUser
python /LazyUser/install.py

# Verificando se a atualização foi bem-sucedida
verificar_sucesso

exit