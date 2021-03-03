print('Vamos fazer uma tabuada?\n')
n = int(input('Digite um número: '))

for i in range(1, 11):
    t = n*i
    print(' {} x {} = {}'.format(n,i,t))