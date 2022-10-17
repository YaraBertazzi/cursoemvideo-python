num = cont = soma = 0
while True:
    num = int(input('Digite um número [ 999 para parar]: '))
    if num == 999:
        break
    soma += num   #se for colocado antes do if ele acaba sendo contado .
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')