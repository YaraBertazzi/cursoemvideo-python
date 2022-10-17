a = int(input('Digite o primero termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
decimo = a + (11 - 1) * r
for c in range (a, decimo, r):
  print('{}'.format(c), end='-> ')
print('Acabou')