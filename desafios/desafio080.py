numeros = []
for i in range(5):
    e = int(input('Digite um valor: '))
    if i == 0 or e > numeros[-1]:
        numeros.append(e)
    else:
        pos = 0
        while pos < len(numeros):
            if e <= numeros[pos]:
                numeros.insert(pos, e)
                break
            pos += 1

           
print(numeros) 
