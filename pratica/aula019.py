pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

pessoas['nome'] = "Rafael"
print(pessoas['nome'])
print(pessoas.keys())
print(pessoas.values())
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil = []

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil[0]['uf'])

estado = dict()
brasil = list()

for c in range(3):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)