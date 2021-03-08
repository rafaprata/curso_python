dezoito = homem = mulher = 0
while True:
    print('VAMOS CADASTRAR ALGUMAS PESSOAS!')
    idade = int(input('Qual a Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    while sexo not in 'mMfF':
        sexo = str(input('Sexo [M/F]: ')).upper()

    if idade > 18:
        dezoito += 1
    if sexo in 'mM':
        homem += 1
    if sexo in 'fF' and idade < 20:
        mulher += 1

    resp = str(input('Você deseja continuar [Y/N]: ')).upper()
    while resp not in 'yYnN':
        resp = str(input('Você deseja continuar [Y/N]: ')).upper()
    if resp in 'nN':
        break

print(f'Foram cadastrados {dezoito} maiores de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'{mulher} mulheres tem menos de 20 anos.')