numeros = [[],[]]

for i in range(7):
    num = int(input(f'Digite o {i+1}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
for i in range(2):
    numeros[i].sort()
print('=-'*30)
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números ímpares digitados foram: {numeros[1]}')