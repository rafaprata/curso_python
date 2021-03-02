print('Vamos converter a base numérica?')
num = int(input('Digite um número: '))

print('Escolha a base que deseja converter:')
select = int(input('1: Binário \n2: Octal \n3: Hexadecimal \n'))

num_convertido = ''

#=== PRIMEIRO TESTE SEM VER A RESOLUÇÃO ===

if num != 0:
    if select == 1:
        while num >= 1:
            resto = str(num % 2)
            num_convertido = resto + num_convertido
            num = int(num/2)
        
        print('O número convertido em binário é {}'.format(num_convertido))
    elif select == 2:
        while num >= 1:
            resto = str(num % 8)
            num_convertido = resto + num_convertido
            num = int(num/8)

        print('O número convertido em octal é {}'.format(num_convertido))
    elif select == 3:
        while num >= 1:
            resto = str(num % 16)
            if int(resto) > 9:
                if int(resto) == 10:
                    resto = 'A' 
                if int(resto) == 11:
                    resto = 'B' 
                if int(resto) == 12:
                    resto = 'C' 
                if int(resto) == 13:
                    resto = 'D' 
                if int(resto) == 14:
                    resto = 'E' 
                if int(resto) == 15:
                    resto = 'F' 
            num_convertido = resto + num_convertido
            num = int(num/16)
        
        print('O número convertido em hexadecimal é {}'.format(num_convertido))
    else:
        print('Você não selecionou uma base, ou digitou errado! \nVamos começar denovo.')
else:
    num_convertido = '0'
    print('O número {} convertido em qualquer base é {}'.format(num, num_convertido)) 