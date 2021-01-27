preco = float(input('Valor (R$): '))
desc = 5

vlrfin = preco*((100-desc)/100)

print('O preço com desconto é R${:.2f}'.format(vlrfin))