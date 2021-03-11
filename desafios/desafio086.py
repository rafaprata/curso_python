matriz = [[],[],[]]

for i in range(3):
    for n in range(3):
        num = int(input(f'Posição [{i}, {n}]: '))
        matriz[i].append(num)

print('=-' *30)
for i in range(3):
    for n in range(3):
        print(f'[ {matriz[i][n]} ]', end=' ')
    print()

