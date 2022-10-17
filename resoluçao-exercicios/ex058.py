import random

tentativa_ac = 0
tentativa_er = 0
soma = 0
usuario = int(input('Adivinhe o numero que estou pensando !!!: '))
comp = random.randint(0, 11)
#print(comp)
while True:
  if usuario == comp:
    tentativa_ac +=1
    soma += 1
    print('acertou')
    break
  else:
    nova = int(input('Você errou , tente mais uma vez, em que número estou pensando: '))
    tentativa_er += 1
    soma = soma + 1
    if nova ==comp:
      print('Acertou')
      break
print('Você teve {} tentativas'.format(soma))



