nome = str(input('Digite seu nome completo: '))

nome = nome.upper().split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))