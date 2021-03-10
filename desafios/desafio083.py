exp = str(input('Digite uma expressão: ')).split()

for expressao in exp:
    if expressao.count('(') != expressao.count(')'):
        print('A expressão não é válida!')
    else:
        print('A expressão é válida!')
print(exp)