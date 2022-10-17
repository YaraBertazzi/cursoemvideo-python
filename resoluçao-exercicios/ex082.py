lista = []
listpar = []
listimpar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listpar.append(n)
    else:
        listimpar.append(n)
    resp = str(input('Quer continuar? [ S/N ] :'))
    if resp in 'Nn':
        break
print(f'Lista geral de números {lista}')
print(f'Lista de números pares {listpar}')
print(f'Lista de números ímpares {listimpar}')

