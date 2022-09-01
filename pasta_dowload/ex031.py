distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    vl = distancia * 0.50
    print('A sua viagem será de {:.2f} R$'.format(vl))
else:
    valor = distancia * 0.45
    print('Como a distancia é muito longa o valor da viagem será {:.2f} R$'.format(valor))
print('Boa viagem!!!')