n1 = float(input('Digite uma medida: '))
n2 = float(input('Digite outra medida: '))
n3 = float(input('Digite a última medida: '))

comp = [n1, n2, n3]
comp.sort()
if comp[2] >= comp[1]+comp[0]:
    print('Não é possível desenhar um triângulo com as medidas\n {}\n {}\n {}'.format(n1, n2, n3))
else:
    print('As medidas formam um TRIÂNGULO!')