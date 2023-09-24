#!/bin/bash

# Defina códigos de escape ANSI para cores
vermelho='\033[0;31m' # Vermelho
verde='\033[0;32m'   # Verde
reset='\033[0m'       # Reset para a cor padrão
amarelo='\033[33m' #Amarelo 
apt-get update -y && apt-get upgrade -y
## lista de pacotes
dependencies=("proot")

for package in "${dependencies[@]}"; do 
    ## Checando ser pacote já foi instalado
    if dpkg -l | grep -q "^ii.*$package "; then
        echo -e "\n${reset}[${verde}*${reset}]${amarelo} $package está instalado.${reset}"
    else    ## Fazendo a instalação do pacote
        echo -e "\n${reset}[${verde}*${reset}] ${verde}Instalando --> $package...${reset}"
        # Substitua o comando abaixo pelo comando apropriado para o seu sistema.
        apt-get install -y "$package"
        
        # Verifique se a instalação foi bem-sucedida
        if [ $? -eq 0 ]; then
            echo -e "\n${reset}[${verde}*${reset}]${verde} $package foi instalado com sucesso.${reset}"
        else
            echo -e "\n${reset}[${vermelho}!${reset}]${vermelho} Falha na instalação de $package.${reset}"
        fi
    fi
done