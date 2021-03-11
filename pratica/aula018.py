#teste = list()
#
#teste.append('Rafael')
#teste.append(22)
#
#galera = list()
#galera.append(teste[:])
#teste[0] = 'Maria'
#teste[1] = 21
#galera.append(teste[:])
#print(galera)

#galera = [['João', 25],['Maria', 22], ['Joaquim',22],['Beth',30]]
##print(galera[3][1])
#
#for p in galera:
#    print(f'{p}')

galera = list()
dado = list()

for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')