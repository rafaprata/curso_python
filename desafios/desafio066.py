s = cont = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f"""Foram digitados {cont} valores.
A soma dos valores é {s}""")