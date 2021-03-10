num = []
par = []
impar = []

while True:
    e = int(input('Digite um valor: '))
    num.append(e)
    if e % 2 == 0:
        par.append(e)
    else:
        impar.append(e)
    
    ans = str(input('Quer continuar? [S/N] '))
    if ans in 'nN':
        break

print(f'Foram digitados os valores {num}')
print(f'Os números pares são {par}')
print(f'Os números ímpares são {impar}')
