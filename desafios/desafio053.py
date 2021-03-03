frase = str(input('Insira a frase:\n')).upper()

#Análise
analise = frase.split()
analise = ''.join(analise)
tam = len(analise)
erro = ''
for i in range(0, tam):
    if analise[i] != analise[tam-(1+i)]:
        erro = 'SIM'
print(frase)
if erro != '':
    print('NÃO é PALÍNDROMO')
else:
    print('É PALÍNDROMO')