vel = float(input('Qual a velocidade do carro: '))

if vel > 80:
    print('== MULTADO ==')
    taxa = vel - 80
    pgto = taxa*7
    print('Você terá que pagar R${:.2f}'.format(pgto))
