frase = str(input('Digite uma frase: '))

a = frase.upper().count('A')
print('Existem {} letras A, nessa frase.'.format(a))

first = frase.upper().find('A')
print('A letra A aparece pela primeira vez como {}º caractere.'.format(first+1))

last = frase.upper().rfind('A')
print('A letra A aparece pela última vez como {}º caractere.'.format(last+1))