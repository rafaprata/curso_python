m = float(input('Digite um valor em metros: '))

dm = m*10
cm = m*100
mm = m*1000

print('dm     cm      mm')
print('{:.3f} {:.3f} {:.3f}'.format(dm,cm,mm))