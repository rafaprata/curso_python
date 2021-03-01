dist = float(input("Digite a distância do trajeto:\n"))

if dist <= 200:
    prec = 0.5*dist

else:
    prec = 0.45*dist

print('O valor da passagem é R${:.2f}'.format(prec))