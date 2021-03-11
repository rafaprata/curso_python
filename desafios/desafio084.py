galera = []
dados = []
maior_peso = menor_peso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    dados.clear()
    ans = str(input('Você deseja continuar? [S/N] '))
    if ans in 'nN':
        break
for i, pessoa in enumerate(galera):
    if i == 0:
        maior_peso = menor_peso = pessoa[1]
    if pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
    if pessoa[1] < menor_peso:
        menor_peso = pessoa[1]

print(f'Foram cadastrados {len(galera)} pessoas.')
print(f'O maior peso foi {maior_peso} Kg. De: ', end='')
for p in galera:
    if p[1] == maior_peso:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi {menor_peso} Kg. De: ', end='')
for p in galera:
    if p[1] == menor_peso:
        print(f'{p[0]} ', end='')
print()