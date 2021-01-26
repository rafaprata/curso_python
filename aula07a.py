n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {} \na multiplicação é {} \na divisão é {:.3f}'.format(s,m,d), end=' ')
#Para criar um número decimal com n casas (flutuantes), indicamos ":.nf" dentro dos {}
#Para não haver quebra de linha dentro de um print indicamos ", end=" no final do print().
#Para criar uma quebra de linha podemos utilizar "\n"
print('Divisão inteira {} e potência {}'.format(di,e))
