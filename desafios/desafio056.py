soma = 0
velho = 0
vinte = 0
for i in range(0, 4):
    print('-='*8)
    nome = str(input('Digite seu NOME: ')).upper()
    idade = int(input('Digite sua IDADE: '))
    sexo = str(input('Digite seu SEXO: ')).upper()

    soma += idade
    if sexo == 'MASCULINO':
        if idade > velho:
            velho = idade
            homem_velho = nome
    if sexo == 'FEMININO':
        if idade < 20:
            vinte += 1

media = soma/4
print('')
print('''Vamos às ANÁLISES:

A MÉDIA de idade é de {:.2f} anos.
O homem mais velho é {}.
E existem {} mulheres com menos de 20 anos.
'''.format(media, homem_velho, vinte))