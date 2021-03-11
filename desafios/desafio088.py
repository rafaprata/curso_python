import random
import time
palpites = []

print('=='*30)
print(f'{"LOTERIA DO RAFÃO":^60}')
print('=='*30)
qtd = int(input('Quantos palpites você quer gerar? '))

print('-='*30)
print(f'{F"SORTEANDO {qtd} NÚMEROS":^60}')
print('-='*30)

for i in range(qtd):
    palpites.append(list())
    while len(palpites[i]) < 6:
        for palpite in palpites[i]:
            if palpites[i].count(palpite) == 2:
                palpites[i].pop()
                break
        num = random.randint(1, 60)
        palpites[i].append(num)
    palpites[i].sort()
    time.sleep(1)
    print(f'O palpite nº {i+1} foi: {palpites[i]}')