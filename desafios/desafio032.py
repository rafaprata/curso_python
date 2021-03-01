print('Vamos descobrir se um ano é BISSEXTO?')
ano = str(input('Digite um ano:\n'))

if ano[3] == 0 and ano[2] == 0:
    if int(ano) % 400 == 0:
        print('É BISSEXTO')
    else:
        print('NÃO É BISSEXTO')
else:
    if int(ano) % 4 == 0:
        print('É BISSEXTO')
    else:
        print('NÃO É BISSEXTO')