print('Gerador de PA')
print('-='* 10)
a = int(input('Digite o primero termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
termo = a #mostra o termo
cont = 1 #conta quantos termos foram
while cont <= 10:
  print('{} -> '.format(termo), end='')
  termo += r
  cont += 1

print('FIM')