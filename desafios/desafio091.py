from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
print('-='*15)
print(f'{"Valores sorteados:":^30}')
print('-='*15)

for i in range(4):
    jogadores[f'Jogador_{i+1}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'    O {k} tirou {v}')
    sleep(1)

print('-='*15)
print(f'{"Ranking":^30}')
print('-='*15)

ranking = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))
i = 1
for k, v in ranking.items():
    print(f'    {i}º Lugar: {k} com {v}.')
    sleep(1)
    i += 1

print(ranking)
