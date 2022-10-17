'''num = 0
cont = 0
soma = 0  como todas essas variaveis receem o mesmo valor (0) posso colocar tudo na mesma linha'''
num = cont = soma = 0
num = int(input('Digite um número [ 999 para parar]: '))  #flag de parada
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [ 999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))