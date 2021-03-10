from random import randint

c0 = randint(1,10)
c1 = randint(1,10)
c2 = randint(1,10)
c3 = randint(1,10)
c4 = randint(1,10)

tupla = (c0,c1,c2,c3,c4)

print(f'Os valores sorteados foram: {c0} {c1} {c2} {c3} {c4}')
print(f'O maior valor sorteado foi: {sorted(tupla)[-1]}')
print(f'O menor valor sorteado foi: {sorted(tupla)[0]}')