alt = float(input('Digite a altura (Metros): '))
larg = float(input('Digite a largura (Metros): '))

area = alt*larg

if area%2 != 0:
    qtd = int((area//2)+1)
else:
    qtd = int(area//2)

print('A área a ser pintada é de {:.2f}m².'.format(area))
print('Serão utilizados {} latas de tinta.'.format(qtd))
