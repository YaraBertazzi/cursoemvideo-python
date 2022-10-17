# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*num):  # recebe varios parametros
    cont = maior = 0
    print('-=' * 30)
    print(f'\nAnalizando os valores passado: ')
    for valor in num:  # para cada valor em num
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        # saber o maior valor
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'E o maior valor informado foi {maior}.')


# Programa Principal
maior(2, 4, 9, 6, 0)
maior(1, 2)
maior(6)
maior()