termo = int(input('PRIMEIRO TERMO DA PA: '))
razao = int(input('RAZÃO DA PA: '))

n_termo = 1
ans = 10
ans_add = 1
while ans_add != 0:
    while n_termo <= ans:
        print('{} > '.format(termo), end='')
        termo = termo + razao
        n_termo += 1
    print('PAUSA')
    ans_add = int(input('Você quer mostrar mais termos? Quantos: '))
    ans += ans_add