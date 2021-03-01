n1 = float(input('Digite o 1º número:\n'))
n2 = float(input('Digite o 2º número:\n'))
n3 = float(input('Digite o 3º número:\n'))

seq = [n1, n2, n3]
seq.sort()

print('O maior valor é {}'.format(seq[0]))
print('O menor valor é {}'.format(seq[2]))