import random
n1 = str(input('Primeiro nome:'))
n2 = str(input('Segundo nome:'))
n3 = str(input('terceiro nome:'))
n4 = str(input('quarto nome:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)   #MUDA A ORDEM DA LISTA ALEATORIAMENTE
print('A ordem é')
print(lista)
