from datetime import date
nasc = int(input('Qual seu ano de nascimento: '))
atual = date.today().year

idade = atual - nasc

if idade < 9:
    print('MIRIM')
elif idade < 14:
    print('INFANTIL')
elif idade < 19:
    print('JÚNIOR')
elif idade < 25:
    print('SÊNIOR')
else:
    print('MASTER')
