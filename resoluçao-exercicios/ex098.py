from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = 1
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
            print('FIM!')


# programa principal
contador(1, 100, 10)
contador(10, 0, 2)
print('Agora é sua vez de contar')
ini = int(input(f'Inicio:'))
fim = int(input(f'Fim: '))
passo = int(input(f'Passo: '))
contador(ini, fim, passo)

