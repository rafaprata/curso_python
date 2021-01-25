#Faça um programa que leia algo pelo teclado e mostre na tela:
# Tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite algo: ')

print('O tipo primitivo de {} é {}'.format(n,type(n)))
print(n.isalnum())
print(n.isalpha())
print(n.isascii())
print(n.isdecimal())
print(n.isdigit())
print(n.isidentifier())
print(n.islower())
print(n.isnumeric())
print(n.isprintable())
print(n.isspace())
print(n.istitle())
print(n.isupper())