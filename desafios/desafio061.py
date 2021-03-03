termo = int(input('PRIMEIRO TERMO DA PA: '))
razao = int(input('RAZÃO DA PA: '))

n_termo = 1
while n_termo <= 10:
    print('{} '.format(termo), end='')
    termo = termo + razao
    n_termo += 1
print('\n')