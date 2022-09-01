#crie um programa que leia um numero real e mostre sua porção inteira
import math
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'. format(num, math.trunc(num)))