import math

cat1 = float(input('Digite o comprimento de um cateto: '))
cat2 = float(input('Digite o comprimento do outro: '))

hip = math.hypot(cat1, cat2)

print('Os catetos {} e {}, tem {} como hipotenusa.'.format(cat1, cat2, hip))