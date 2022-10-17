lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:  # n nao estiver na lista
        lista.append(n)
        print('Valor adicionado co sucesso!!!')
    else:
        print('Valor duplicado! Não vou adicionar.')

    r = str(input('Quer continuar?[S/N]: '))
    if r in 'Nn':
        break
print(lista)
print('-=' * 25)
lista.sort()
print(f'Você digitou os valores {lista}')