import random
import time

print("Bem vindo ao Jogo da Advinhação")
play = str(input('Vamos jogar um jogo? (Y/N)\n'))

play = play.upper()
if play == 'YES':
    print('Deixa eu pensar em um número...')
    time.sleep(2)
    num = random.randint(0, 5)
    print('Pronto!')
    print('Eu pensei em um número de 0 a 5, inteiro!')
    ans = int(input('Que número eu pensei?\n'))
    if ans == num:
        print('Você disse que eu pensei {}'.format(ans))
        print('Você acertou!')
        print('Parabéns!')
    else:
        print('Você disse que eu pensei {}'.format(ans))
        print('Mas na verdade eu pensei {}'.format(num))
        print('Você não acertou dessa vez.')
        print('Vamos jogar denovo?')
else:
    print('OK...')
print('Te vejo depois!')
