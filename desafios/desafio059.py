n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

opcao = 0
while opcao != 5:
    print('''Escolha uma opção:
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair
    ''')
    opcao = int(input('Sua escolha: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos valores é: {}'.format(soma))
    if opcao == 2:
        multi = n1 * n2
        print('A multiplicação dos valores é: {}'.format(multi))
    if opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('O maior número é: {}'.format(maior))
    if opcao == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))     