#!/usr/bin/env python
"""_____________________________________________________
+=[ BY: AstralSecHaxor from BRAZIL :)
+=[ Version: 1.0 - beta
+=[ YouTube: https://youtube.com/@AstralSec_Haxor
+=[ Github: https://github.com/AstralSecHaxor/LazyUser
——————————————————————————————————————————————————————
SCRIPT DO USUÁRIO 
AQUI ESTARÃO TODAS AS FUNÇÕES DAS CATEGORIAS 
QUE O USUÁRIO USARÁ PARA NAVEGAR PELO TOOL."
"""
import os
from time import sleep as timeout
from modules.gerenciador import *
from modules.logos import *
from os.path import isdir


# Defina códigos de escape ANSI para cores
vd = "\33[1;36m" # Ciano
vlh = "\33[1;31m" #vermelho 
bra = "\33[1;37m" # branco
az = "\033[34m" # Azul
ma = "\033[35m" #Magento
am = "\033[33m" #Amarelo 


def check_proot():
    
    if isdir("/etc/apt") == True:
        print(f"{bra}[{vd}*{bra}] {vd}Termux-chroot está ativo.");timeout(1)
        banner_inicial()
        while True:
            try:
                lazyscript = input(f"{vd}LazyUser ~$ {bra}")
                option_control  = lazyscript.replace(" ", "")
                
            except KeyboardInterrupt:
                sair_do_programar().exit()
            except EOFError:
                sair_do_programar().exit()
                    
            
            ## Categoria: Coletar de informações
            if option_control == "1" or option_control == "01":
                coletar_informacoes()
                
                
            ## Categoria: análise de vulnerabilidades
            elif option_control == "2" or option_control == "02":
                analise_vulnerabilidades()
            
            ## Categoria: Web Hacking
            elif option_control == "3" or option_control == "03":
                web_hacking()
                
            ## Categoria: Avaliações de Banco de dados.
            elif option_control == "4" or option_control == "04":
                avaliacoes_databases()
                
            ## Categoria: Ataque Senhas
            elif option_control == "5" or option_control == "05":
                ataque_senhas()
            
            ## Categoria: ataques Sem Fio
            elif option_control == "6" or option_control == "06":
                ataque_sem_fio()
                
            
            elif option_control == "x" or option_control == "X": atualizar() ## Opção de atualização do LazyUser
            elif option_control == "00" or option_control =="0": sair_do_programar() ## Sair do Script
            
            else:
                print(f"{vlh}\nUps! Você tentou inserir uma opção que não existe :({b}");timeout(1);
                banner_inicial()

        
    else:
        print(f"""
{bra}[{vlh}!{bra}]{vlh} Termux-chroot não encontrado. O script não pode ser executado.
    
  {bra}{am}User{bra}: Utilize esses comandos para evitar erros inesperados antes da execução do script.
  
    {am}Exemplo{bra}:
        $ {am}termux-chroot{bra}: Cria um ambiente de chroot temporário no Termux, mudando temporariamente o diretório raiz para um local especificado.
        $ {am}unset LD_PRELOAD{bra}: Remove a variável LD_PRELOAD para garantir que programas no ambiente de chroot do Termux não usem bibliotecas incompatíveis do sistema host.
   
   """)
        sys.exit()
check_proot()

