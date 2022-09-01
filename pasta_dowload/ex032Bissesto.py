from datetime import date
ano = int(input('Que ano quer analisar?Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year  #ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:   #todo ano divisivel por 4 é bissexto, de 100 não é bissexto e por 400 é bissexto
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))