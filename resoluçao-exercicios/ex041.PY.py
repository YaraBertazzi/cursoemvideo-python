from datetime import date
atleta = int(input('Digite o ano de nascimento do atleta: '))
hoje = date.today()
ano = hoje.strftime('%Y')
id = int(ano) - atleta
print(id)

if id <= 9 :
    print('Categoria : MIRIM ')
elif id >= 10 and id <= 14 :
    print('Categoria: INFATIL')
elif id >= 15 and id <= 19 :
    print('Categoria: JÚNIOR')
elif id >= 20 and id <= 25 :
    print('Categoria: SÊNIOR')
elif id > 25:
    print('Categoria: MASTER')