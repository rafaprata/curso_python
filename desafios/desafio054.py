import datetime

maior = 0
menor = 0
for i in range(0, 7):
    nasc = int(input('Ano de Nascimento: '))
    idade = datetime.date.today().year - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são MAIORES de idade.'.format(maior))
print('{} pessoas são MENORES de idade.'.format(menor))
