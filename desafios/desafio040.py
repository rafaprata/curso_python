n1 = float(input('Digite a 1ª Nota: '))
n2 = float(input('Digite a 2ª Nota: '))

m = (n1 + n2)/2

if m >= 7.0:
    print('APROVADO! Nota: {:.2f}'.format(m))
elif 5 <= m < 7:
    print('RECUPERAÇÃO! Nota: {:.2f}'.format(m))
else:
    print('REPROVADO! Nota: {:.2f}'.format(m))