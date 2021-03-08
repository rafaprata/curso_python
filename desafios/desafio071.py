print('=-'*20,'\n')
resto = int(input('Qual o valor você deseja retirar: R$ '))
print('=-'*20,'\n')

c50 = c20 = c10 = c1 = 0

while resto != 0:
    c50 = resto // 50
    resto = resto % 50
    c20 = resto // 20
    resto = resto % 20
    c10 = resto // 10
    c1 = resto % 10
    resto = resto%1

#print(c50, c20, c10, c1)

print('Você vai retirar:')
if c50 != 0:
    print(f'[{c50}] notas de R$50.00')
if c20 != 0:
    print(f'[{c20}] notas de R$20.00')
if c10 != 0:
    print(f'[{c10}] notas de R$10.00')
if c1 != 0:
    print(f'[{c1}] notas de R$1.00')
