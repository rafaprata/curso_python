import random
import time
from os import system

print('Vamos JOGAR um jogo?')
r = str(input('[Y/N]: '))

while r in 'yY':
    print('''== O JOGO funciona assim: ==
    [1] Eu vou pensar em um número [0 - 10].
    [2] E você vai tentar descobrir.
    [3] Se você não acertar, tenta de novo.
    [4] O score é a quantidade de tentativas.''')
    time.sleep(1)
    print('Vamos lá...')
    time.sleep(2)
    computador = random.randint(0, 10)
    print('PRONTO!')
    print('Agora é sua vez!')

    player = int(input('Que número eu pensei: '))
    tentativas = 1

    while player != computador:
        tentativas += 1
        print('Hmmm...')
        time.sleep(1)
        print('Você ERROU!')
        player = int(input('Tente novamente: '))

    print('Hmmm...')
    time.sleep(1)
    print('Você ACERTOU!')
    print('=== SCORE: {} ==='.format(tentativas))
    r = str(input('Você quer jogar de novo [Y/N]: '))
    while r not in 'yYnN':
        r = str(input('Você quer jogar de novo [Y/N]: '))
    system('clear')
print('Bom, até mais! TCHAU!')