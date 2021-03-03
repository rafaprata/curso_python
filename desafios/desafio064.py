n = 0
soma = 0
qtd = -1
while n != 999:
    soma += n
    qtd += 1
    n = int(input('Digite um número: '))

print('Foram digitados {}'.format(qtd))
print('A soma dos números é {}'.format(soma))