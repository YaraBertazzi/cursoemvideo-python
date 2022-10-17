maior = 0
menor = 0
for p in range (1, 6):
  peso = float(input('Digite o peso da {}° pessoa: '.format(p)))
  if p == 1: #1°sentença tera o maior eo menor peso
    maior = peso
    menor = peso
  else:
    if peso > maior: #se o peso for maior que o primeiro maior peso, esse novo peso passa a ser maior
      maior = peso
    if peso < menor: #se o peso for menor que o primeiro menor peso, esse novo peso passa a ser o menor
      menor = peso
print('O maior peso lido foi de {} kg'.format(maior))
print('O menor peso lido foi de {} kg'.format(menor))

#se p for o 1° ele sera maior ou menor , se não peso maior sera = ao peso. se peso menor for menor que peso , ele sera o menor .
