import datetime

ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    tempo = 18 - idade
    print('Faltam ainda {} anos para se alistar.'.format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Fazem {} anos que passou o prazo.'.format(tempo))
else:
    print('Está no ano de se alistar!')