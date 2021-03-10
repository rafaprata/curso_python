numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))

    ans = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if ans in 'nN':
        break

numeros.sort(reverse=True)
print()
print(f'Foram digitados {len(numeros)} numeros.')
print(f'A lista digitada é a seguinte: {numeros}')
if 5 in numeros:
    print('O número 5 foi digitado e está na lista!')
else:
    print('O número 5 não foi digitado e não está na lista!')