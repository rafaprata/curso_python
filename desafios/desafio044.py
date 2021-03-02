print('===== LOJA =====')
valor = float(input('Quanto voce gastou: R$'))
print('''Qual é a opção de pagamento:
[1] À vista Dinheiro/Cheque
[2] À vista Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    desc = 10/100
    vlr_final = valor - (valor*desc)
    print('Sua compra de R${:.2f} vai sair por R${:.2f}'.format(valor,vlr_final))
elif opcao == 2:
    desc = 5/100
    vlr_final = valor - (valor*desc)
    print('Sua compra de R${:.2f} vai sair por R${:.2f}'.format(valor, vlr_final))
elif opcao == 3:
    parc = 2
    vlr_parc = valor/parc
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f}, SEM JUROS!'.format(valor,vlr_parc))
elif opcao == 4:
    juros = 20/100
    parc = int(input('Quantas parcelas: '))
    vlr_final = valor +(valor*juros)
    vlr_parc = vlr_final/parc
    print('Sua compra de R${:.2f} será parcelada em {}x de R${:.2f}'.format(valor, parc, vlr_parc))
else:
    print('Você não escolheu uma opção válida!')