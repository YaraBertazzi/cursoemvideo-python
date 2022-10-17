import linecache
import random
import time
print('VAMOS JOGAR JOKENPÔ.... ')
opcao = str(input('Escolha: "Pedra", "Papel" ou "Tesoura": '))
computador = random.choices(("Pedra", "Papel", "Tesoura"))
print('PENSANDO....')
time.sleep(2)
#computador = random.choices(escolha)
print(computador)
if opcao == computador :
    print('GANHEI !!!!')
else:
    print('PERDI !!!')

