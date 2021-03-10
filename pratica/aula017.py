num = [1, 2, 3, 5]
print(num)
num[2] = 5
print(num)
num.append(7)
print (num)
num.sort(reverse=True)
num.insert(2, 0)
num.pop()
print(num)
num.remove(0)
if 4 in num:
    num.remove(4)
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = list()

valores.append(5)
valores.append(7)
valores.append(9)

for i, valor in enumerate(valores):
    print(f'Na posição {i}, encontrei {valor}!')

a = [2,3,4,5]
b = a[:] #Cópia de uma lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')