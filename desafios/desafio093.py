import time
analise = {}
soma_gols = 0

analise['jogador'] = str(input('Nome do Jogador: '))
qtd_jogos = int(input(f'Quantos jogos foram jogados: '))
analise['gols'] = list()

for i in range(qtd_jogos):
    analise['gols'].append(int(input(f'Quantos gols foram feitos na partida {i+1}: ')))
    soma_gols += analise['gols'][i]
analise['total'] = soma_gols

time.sleep(1)

print('-='*30)
print(analise)
print('-='*30)

for k, v in analise.items():
    print(f'O campo {k} tem valor {v}')

print('-='*30)
time.sleep(1)
for k, v in enumerate(analise['gols']):
    print(f'    No jogo {k+1} {analise["jogador"]} fez {v} gols.')
    time.sleep(1)
    