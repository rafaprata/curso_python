matriz = [[],[],[]]
soma_par = soma_terceira = maior_segunda = 0
for i in range(3):
    for n in range(3):
        num = int(input(f'Posição [{i}, {n}]: '))
        matriz[i].append(num)
        if num % 2 == 0:
            soma_par += num
        if n == 2:
            soma_terceira += num
        if i == 1:
            if n == 0 or num > maior_segunda:
                maior_segunda = num

print('=-' *30)
for i in range(3):
    for n in range(3):
        print(f'[ {matriz[i][n]} ]', end=' ')
    print()
print('-='*30)
print(f'A soma dos números pares é {soma_par}.')
print(f'A soma da 3ª coluna é {soma_terceira}.')
print(f'O maior valor da 2ª linha é {maior_segunda}')