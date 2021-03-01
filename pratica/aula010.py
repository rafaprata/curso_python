#nome = str(input('Qual é o seu nome: '))
#
#if nome == 'Gustavo':
#    print('Que nome zuado.')
#else:
#    print('Seu nome é legal!')
#print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2
print('A sua média foi {}'.format(m))
if m >= 6:
    print('Voce foi aprovado. :D')
else:
    print('Você foi reprovado. :(')