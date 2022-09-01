num = int(input('Digite um número: '))
resto = num % 2
if resto == 0:
    print('{} é um número PAR!'.format(num))
else:
    print('{} é um número ÍMPAR!'.format(num))