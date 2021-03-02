nome = str(input('Qual é o seu nome:\n'))

if nome == 'Rafael':
    print('Seu nome é maravilhoso!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Laura':
    print('Que belo nome feminino!')
#else:
#    print('Massa!')

print('Tenha um bom dia, {}!'.format(nome))