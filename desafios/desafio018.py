import math
ang = float(input('Digite o valor de um ângulo:  '))

ang_rad = math.radians(ang)

sen = math.sin(ang_rad)
cos = math.cos(ang_rad)
tg = math.tan(ang_rad)

print('O ângulo {}° tem:\n - Seno = {:.2f}\n - Cosseno = {:.2f}\n - Tangente = {:.2f}'.format(ang,sen,cos,tg))

#Fiquei com dúvida de como avisar quando o angulo for 90, 270 ou seus múltiplos, já que não existe tangente!