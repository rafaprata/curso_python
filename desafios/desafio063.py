n = int(input('Digite um número: '))

seq = 0
termo_ultimo = 0
termo_penultimo = 0

while seq < n:
    print('{} '.format(termo_ultimo), end='')
    
    if termo_ultimo+termo_penultimo < 2:
        termo_penultimo = termo_ultimo
        termo_ultimo = 1
    else:
        soma = termo_ultimo + termo_penultimo
        termo_penultimo = termo_ultimo
        termo_ultimo = soma
    seq += 1
print('')