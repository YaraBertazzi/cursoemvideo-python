print('\033[1;32m-=\033[m'*20)
print('\033[1;32mAnalisador de Triângulo\033[m')
print('\033[1;32m-=\033[m'*20)
r1 = float(input('Segmento um:'))
r2 = float(input('Segmento dois: '))
r3 = float(input('Segmento três: '))
if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('Esses segmentos PODEM formar um triângulo !!!')
else:
    print('Esses segmentos NÃO PODEM formar um triângulo.')