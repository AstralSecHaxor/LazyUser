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
    echo -e "\n[${verde}*${reset}] Comando executado com sucesso."
  else
    echo -e "\n[${vermelho}!${reset}] Falha na execução do comando."
    echo -e "\n[${vermelho}!${reset}] Lamento, mas não foi possível continuar :("
    exit 1
  fi
}

# Atualiza a lista de pacotes e faz o upgrade
echo -e "\n[${verde}*${reset}] Atualizando lista de pacotes e fazendo upgrade..."
apt-get update -y && apt-get upgrade -y
# Verificando se a atualização foi bem-sucedida
verificar_sucesso

# Lista de pacotes
dependencies=("proot" "git" "python" "python3")

for package in "${dependencies[@]}"; do
    ## Checando se o pacote já foi instalado
    if dpkg -l | grep -q "^ii.*$package "; then
        echo -e "\n[${verde}*${reset}] $package está instalado."
    else
        ## Fazendo a instalação do pacote
        echo -e "\n[${verde}*${reset}] Instalando --> $package..."
        # Comando de instalação dos pacotes
        apt-get install -y "$package"
        # Verifique se a instalação foi bem-sucedida
        verificar_sucesso
    fi
done

# Clona o repositório LazyUser e executa install.py
echo -e "\n[${verde}*${reset}] Clonando o repositório 'LazyUser' e executando 'install.py'..."
git clone https://github.com/AstralSecHaxor/LazyUser
# Verifique se a clonagem foi bem-sucedida
verificar_sucesso

# Você pode descomentar esta linha quando estiver pronto para executar install.py
# echo -e "\n[${verde}*${reset}] Executando 'install.py'..."
python3 LazyUser/install.py

echo -e "\n[${verde}*${reset}] Tudo foi concluído com sucesso!"
exit

#wget -O script.sh https://raw.githubusercontent.com/usuario/repositorio/master/script.sh && chmod +x script.sh && ./script.sh