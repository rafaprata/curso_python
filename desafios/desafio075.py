n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tupla = (n1,n2,n3,n4)
print(f'Você digitou os valores {tupla}')

nove = tupla.count(9)
print(f'O número 9 apareceu {nove} vezes.')

if tupla.count(3) != 0:
    tres = tupla.index(3) + 1
    print(f'O número 3 foi digitado primeiro na {tres}ª posição.')
else:
    print('Não foi digitado o número 3')

print('Os valores pares digitados foram:', end=' ')
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')
