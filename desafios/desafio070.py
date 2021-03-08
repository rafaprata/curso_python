total = 0
mais_1000 = 0
mais_barato_nome = ''
mais_barato_preço = 0

while True:
    nome = str(input('Nome do Produto: ')).upper()
    preço = float(input('Preço: R$ '))

    if mais_barato_preço == 0:
        mais_barato_preço = preço
        mais_barato_nome = nome
    elif preço < mais_barato_preço:
        mais_barato_preço = preço
        mais_barato_nome = nome

    if preço > 1000:
        mais_1000 += 1
    
    total += preço    

    resp = str(input('Você quer continuar [Y/N]: '))
    while resp not in 'yYnNsS':
        resp = str(input('Você quer continuar [Y/N]: '))
    if resp in 'nN':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'{mais_1000} produtos custam mais de R$1000.00.')
print(f'O produto mais barato foi {mais_barato_nome}, custando R${mais_barato_preço:.2f}')