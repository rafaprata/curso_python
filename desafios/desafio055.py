maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input('Digite seu peso em Kg: '))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('')
print('O menor peso é {}Kg.'.format(menor))
print('O maior peso é {}Kg.'.format(maior))