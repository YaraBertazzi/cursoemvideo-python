# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jog='<Desconhecido>', gols=0):
  print(f'O jogador {jog} fez {gols}')


n = str(input('Nome do jogador: '))
g = str(input('número de gols: '))
#if g.isnumerc():
 #g = int(g)
#else:
  #gols = 0
if n.strip() == '':
  ficha(gols=g)
else:
  ficha(n, g)
