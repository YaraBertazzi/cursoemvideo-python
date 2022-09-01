import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digito o valor do cateto adjacente: '))
#hi = (co**2 + ca **2) ** (1/2)
#print('Com o cateto oposto de {} e cateto adjacente {}, a hipotenusa é {}'.format(co, ca, hi))
hi = math.hypot(co,ca)
print('Hipotenusa é = {:.2f}'.format(hi))
