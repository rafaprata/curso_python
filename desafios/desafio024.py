cidade = str(input('Cidade: '))

cidade = cidade.upper()

santo = 'SANTO' == cidade.split()[0]

print('A cidade {} começa com "SANTO": {}'.format(cidade, santo))