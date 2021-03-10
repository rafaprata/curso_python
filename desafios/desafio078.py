numero = list()
maior = menor = 0
for i in range(0, 5):
    numero.append(int(input(f'Digite um valor na posição {i}: ')))
    if i == 0:
        maior = menor = numero[i]
    else:
        if numero[i] > maior:
            maior = numero[i]
        if numero[i] < menor:
            menor = numero[i]

print(f'Você digitou os valores {numero}')
print(f'O maior valor foi {maior}, nas posições: ', end='')
for i, v in enumerate(numero):
    if v == maior:
        print(f'{i} ',end='')
print()
print(f'O menor valor foi {menor} nas posições: ', end='')
for i, v in enumerate(numero):
    if v == menor:
        print(f'{i}', end='')
print()
