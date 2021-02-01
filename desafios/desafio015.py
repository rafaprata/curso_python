km = float(input('Quantos Km foram percorridos: '))
dias = int(input('Quantos dias foi alugado: '))

aluguel_dia = dias*60
aluguel_km = km*0.15

pagar = aluguel_dia + aluguel_km

print('Foram percorridos {:.2f}Km, resultando o valor de R${:.2f}'.format(km, aluguel_km))
print('O carro foi alugado por {} dias, resultando o valor de R${:.2f}'.format(dias, aluguel_dia))
print('O valor total é de R${:.2f}'.format(pagar))