n = int(input('Digite um número: '))
tot = 0 #contador
for c in range(1, n + 1):
  if n % c == 0:
    print('\033[33m', end=' ')  #amarelo
    tot += 1
  else:
    print('\033[31m', end=' ')  #vermelho
  print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
  print('E por isso ele É PRIMO!')
else:
  print('E por isso ele NÃO É PRIMO!')
