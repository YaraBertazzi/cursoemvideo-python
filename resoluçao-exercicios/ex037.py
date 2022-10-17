import random

num = int(input('Digite um numero inteiro: '))
conversao = int(input('Escolha aconversão. Digite: 1- Binári, 2- Octal, 3- Hexagonal: '))

if conversao == 1:
    bi = bin(num)
    print(f'O numero {num} em Biário é: {bi}')

elif conversao == 2:
    oc = oct(num)
    print(f'O numero {num} em Octual é: {oc}')

elif conversao == 3:
    hexa = hex(num)
    print(f'O numero {num} em Hexadecimal é: {hexa}')

elif conversao != 1 and conversao != 2 and conversao != 3:
    print('Digite uma opção valida')

