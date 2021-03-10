lista = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.9,
    'Estojo', 25
)
#print(lista)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for i in range(0,len(lista),2):
    lenth = len(lista[i])
    print(f'{lista[i]:.<30}','R$'+f'{lista[i+1]:>7.2f}')