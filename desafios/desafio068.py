from random import randint

vitorias = 0
while True:
    print('=-='*6)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-='*6)

    n_jog = int(input('Digite um valor: '))
    n_comp = randint(0, 10)

    s = n_jog + n_comp

    paridade = s % 2

    jogada = str(input('PAR ou ÍMPAR [P/I]: ')).upper()
    print('---'*6)

    if jogada in 'P':
        jogada = 0
    else:
        jogada = 1

    print(f'Você jogou {n_jog} e o computador {n_comp}. Total {s}.')

    if paridade != jogada:
        print('Você PERDEU!')
        print('-=-'*6)
        break
    
    print('Você VENCEU!')
    print('-=-'*6)
    vitorias += 1
    

print(f'GAME OVER! Você venceu {vitorias} vezes.')