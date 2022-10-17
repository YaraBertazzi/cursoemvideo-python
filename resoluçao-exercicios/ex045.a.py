from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
     [ 0 ] Pedra
     [ 1 ] Papel
     [ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada:'))
print('-*' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
print('-*' * 11)

if computador == 0:  # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')

elif computador == 1:  # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')

elif computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR GANHA')
    elif jogador == 1:
        print('COMPUTADOR GANHA')
    elif jogador == 2:
        print('EMPATE')