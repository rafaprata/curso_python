lista = []
i = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    
    while lista.count(lista[i]) > 1:
        lista.pop()
        print('Número já adicionado!',end=' ')
        lista.append(int(input('Digite outro valor: ')))

    ans = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if ans in 'nN':
        break

    i += 1
lista.sort()
print(lista)