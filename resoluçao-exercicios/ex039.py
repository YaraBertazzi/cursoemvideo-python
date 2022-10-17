from datetime import date
nasc = int(input('Digite o ano do seu nascimento: '))
hoje = date.today()
ano = hoje.strftime('%Y')
id = int(ano) - nasc
#print(id)
if id < 18:
    temp = 18 - id
    print(f'Você tem {id} anos, ainda faltam {temp} anos , para poder se alistar!')

elif id == 18:
    print('Você ja esta na idade de se alistar!')

elif id > 18:
    print('Pasou do ano de se alistar')




