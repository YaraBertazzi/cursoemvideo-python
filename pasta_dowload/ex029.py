velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[4;31mVocê excedeu o limite permitido de 80 km/h\033[m')
    multa = (velocidade - 80) * 7
    print('\033[4;31mDeve pagar uma multa de {} R$\033[m'.format(multa))
print('Dirija com segurança!!!')