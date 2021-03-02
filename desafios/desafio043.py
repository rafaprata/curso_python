alt = float(input('Altura (m e cm): '))
peso = float(input('Peso (Kg): '))

imc = peso/(alt**2)

print('Você está: ')
if imc < 18.5:
    print('Acima do Peso')
elif imc < 25:
    print('Peso Ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')