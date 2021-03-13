import datetime

cadastro = {}


cadastro['nome'] = str(input('Nome: '))
cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()

while cadastro['sexo'] not in 'mMfF':
    del(cadastro['sexo'])
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()

ano = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.date.today().year - ano
cadastro['ctps'] = str(input('Carteira de Trabalho (0 caso não tenha): '))

if cadastro['ctps'] != '0':
    cadastro['ano de contratacao'] = int(input('Ano de contratação: '))
    tempo_contribuicao = datetime.date.today().year - cadastro['ano de contratacao']
    cadastro['salario'] = float(input('Salário: '))
    if cadastro['sexo'] in 'mM':
        if tempo_contribuicao >= 20:
            cadastro['idade de aposentar'] = cadastro['idade']
        else:
            restante = 20 - tempo_contribuicao
            cadastro['idade de aposentar'] = cadastro['idade'] + restante
    else:
        if tempo_contribuicao >= 15:
            cadastro['idade de aposentar'] = cadastro['idade']
        else:
            restante = 15 - tempo_contribuicao
            cadastro['idade de aposentar'] = cadastro['idade'] + restante

print('-='*30) 
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}.')
print(cadastro)