from random import randint   #sorteia um numero dentro dos parametros
from time import sleep    #faz o computador esperar
computador = randint(0, 5)   #faz o computador 'pensar'
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinha...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinha
print('PROCESSANDO....')
sleep(3)   #espera 3 segundos
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
