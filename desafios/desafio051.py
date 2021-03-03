primeiro = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('A PA de {} tomados a cada {} vezes:\n'.format(primeiro,razao))
for i in range(primeiro, razao*10 + primeiro, razao):
    print(i)