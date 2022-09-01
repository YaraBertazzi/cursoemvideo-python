import math
an = float(input('Digite um ângulo: '))
se = math.sin(math.radians(an))   #math.rafians converte em angulo/grau
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print('Ângulo: {:.2f},\n Seno: {:.2f},\n Cosseno: {:.2f},\n Tangente: {:.2f}'.format(an, se, co, ta))