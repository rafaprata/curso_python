sal = float(input('Digite seu salário:\n'))

if sal > 1250:
    taxa = 0.1
else:
    taxa = 0.15

aum = sal * taxa
novo_sal = sal + aum
print('O aumento é de R${:.2f}\nSeu novo salário é R${:.2f}'.format(aum, novo_sal))