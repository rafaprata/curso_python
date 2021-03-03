sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while sexo not in 'MF':
   sexo = str(input('Dados inválidos! Informe o sexo [M/F]: ')).upper()

print('Seu sexo é {}'.format(sexo))