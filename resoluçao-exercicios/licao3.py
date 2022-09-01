a = int(input('Primeiro bimestre:'))
b = int(input('Segundo bimestre:'))
c = int(input('Terceiro bimestre'))
d = int(input('Quarto bimestre:'))
media = (a + b + c + d)/ 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('A media é {}'.format(media))
else:
    print('Alguma nota foi informada errado')