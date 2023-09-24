#!/bin/bash

# Verifica se o arquivo "/etc/os-release" existe
if [ -e /etc/os-release ]; then
    # Lê o conteúdo do arquivo "/etc/os-release"
    source /etc/os-release
    
    # Verifica se a variável "ID" contém alguma das distribuições desejadas
    if [[ $ID == "kali" || $ID == "ubuntu" || $ID == "debian" || $ID == "parrot" ]]; then
        echo "$ID"
    else
        echo "Desconhecido"
    fi
else
# Verificar se é o Termux
    if [[ $(uname -o) == "Android" ]]; then
    echo "termux"
    else
        echo "Desconhecido"
    fi
fi