qtd = 0
maior = 0
menor = 0
play = 'S'
s = 0

while play in 'sS':
    n = int(input('Digite um número: '))
    s += n
    if maior == 0 or n > maior:
        maior = n
    if menor == 0 or n < menor:
        menor = n
    qtd += 1

    play = str(input('Quer continuar [S/N]: '))
media = s/qtd
print(maior, menor, media)