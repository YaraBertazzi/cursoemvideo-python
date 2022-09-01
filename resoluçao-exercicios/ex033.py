a = int(input('Digite um número: '))
b = int(input('Digite segundo número: '))
c = int(input('Digite terceiro número: '))
menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>c and b>a:
    maior = b
if c>a and c>b:
    maior = c
print('Dos número que digitou o menor é {} eo maior é {}'.format(menor, maior))