n1 = float(input('Digite uma medida: '))
n2 = float(input('Digite outra medida: '))
n3 = float(input('Digite a última medida: '))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('É possível formar um TRIÂNGULO')
    if n1 == n2 and n1 == n3 and n2 == n3:
        print('Esse é um Triângulo EQUILÁTERO!')
    elif n1 == n2 or n1 == n2 or n2 == n3:
        print('Esse é um Triângulo ISÓSCELES!')
    else:
        print('Esse é um Triângulo ESCALENO!')
else:
    print('As medidas NÃO formam um TRIÂNGULO!')