n = int(input('Digite um numero para calcular seu fatorial: '))
c = n #contador começa pelo numero que eu quero saber o fatorial
f = 1
print('Calculando {}!:'.format(n))
while c > 0 :
  print('{} '.format(c), end='')
  print('x ' if c > 1 else '= {} '.format(f), end='')
  f *= c
  c -= 1

print('\nO fatorial de {} é {}'.format(n, f))
