print('Qual a temperatura hoje?')

tc = float(input('Digite a temperatura em °C: '))

tf = (tc*9)/5+32

print('A temperatura {:.2f}°C, corresponde a {:.2f}°F.'.format(tc,tf))