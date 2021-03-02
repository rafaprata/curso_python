casa = float(input('Qual o valor da Residência: R$'))
salario = float(input('Qual é o seu salário: R$'))
prazo = int(input('Quantos anos para pagar: '))

prestacao = casa / (prazo*12)

if prestacao > 0.3*salario:
    print('Seu empréstimo foi NEGADO.')
    print('O valor da prestação é de R${:.2f}.'.format(prestacao))
else:
    print('Seu empréstimo foi APROVADO!')
    print('O valor da prestação é de R${:.2f}.'.format(prestacao))