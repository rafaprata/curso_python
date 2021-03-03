n = int(input('Digite um número: '))
tot = 0
for i in range(1, n + 1):
    if (n%i) == 0:
        print('[{}] '.format(i), end = '')
        tot += 1
    else:
        print('{} '.format(i), end = '')
print('\nO número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('Por isso número é PRIMO.')
else:
    print('Por isso número NÃO é PRIMO.')