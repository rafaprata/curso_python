nome = str(input('Digite seu nome completo: '))

nome = nome.title()

print(nome.upper())
print(nome.lower())

qtd = len(nome)-nome.count(' ')

print('{} tem {} letras.'.format(nome, qtd))

dividido = nome.split()

print('{} tem {} letras.'.format(dividido[0],len(dividido[0])))