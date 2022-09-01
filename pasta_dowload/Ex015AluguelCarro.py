dia = int(input('Dias alugado:'))
Km = float(input('Km rodado nos dias alugados:'))
pago = (dia * 60.00) + (Km * 0.15)
print('O valor a ser pago é,{:.2f} R$'.format(pago))