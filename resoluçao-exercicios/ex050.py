soma = 0  #acumulador
cont = 0  #contador
for n in range(1,7):
  n1 = int(input('Digite um numero inteiro: '))
  if n1 % 2 ==0:
    soma += n1
    cont += 1
print('Você digitou {} números PARES e a soma foi {}'.format(cont, soma))