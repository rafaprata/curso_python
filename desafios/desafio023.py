num = str(input('Digite um número de 0 a 9999: '))

num = '000'+num

u = num[len(num)-1]
d = num[len(num)-2]
c = num[len(num)-3]
m = num[len(num)-4]

print(num)
print('UNIDADE: {} \nDEZENA: {} \nCENTENA: {} \nMILHAR: {}'.format(u, d, c, m))
