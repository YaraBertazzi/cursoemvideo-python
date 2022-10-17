from datetime import date
atual = date.today().year
cont = 0
soma = 0
for c in range(0, 7):
  nasc = int(input('Digite seu ano de nascimento: '))
  ano = atual - nasc
if ano >= 18:
  cont = c + 1
  print('{} atingiram a maioridade'.format(cont))

elif ano < 18:
  cont = c + 1
  print('{} não atingiram a maioridade'.format(cont))

