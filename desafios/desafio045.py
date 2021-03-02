#Jogo de Jokenpô
import random
import time
from os import system

system('clear')
print('''Vamos Jogar JOKENPÔ!!!
As regras:
[1] - Pedra
[2] - Papel
[3] - Tesoura''')
jog_opcao = int(input('Você escolhe: '))

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!')
time.sleep(1)
print('')

comp_opcao = random.randint(1,3)

if jog_opcao != comp_opcao:
    if jog_opcao == 1:
        if comp_opcao == 2:
            print('Eu escolhi PAPEL.\nGANHEI!')#perdemos: papel ganha de pedra
        elif comp_opcao == 3:
            print('Eu escolhi TESOURA.\nVOCÊ GANHOU!')#ganhamos: pedra ganha de tesoura
    elif jog_opcao == 2:
        if comp_opcao == 1:
            print('Eu escolhi PEDRA.\nVOCÊ GANHOU!')#ganhamos: papel ganha de pedra
        elif comp_opcao == 3:
            print('Eu escolhi TESOURA.\nGANHEI!')#perdemos: tesoura ganha de papel
    elif jog_opcao == 3:
        if comp_opcao == 1:
            print('Eu escolhi PEDRA.\nGANHEI!')#perdemos: pedra ganha de tesoura
        elif comp_opcao == 2:
            print('Eu escolhi PAPEL.\nVOCÊ GANHOU!')#ganhamos: tesoura ganha de papel
else:
    print('EMPATAMOS!')
