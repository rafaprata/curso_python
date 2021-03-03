n = int(input('Digite um número: '))
factorial = 1
while n > 1:
    factorial = factorial * n
    n = n - 1
print('Seu Fatorial: {}'.format(factorial))