expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0: #pilha for maior que zero
      pilha.pop() #retira o ultimo
    else:
      pilha.append(')')
      break
if len(pilha) == 0:
  print('Sua expressão está válida!')
else:
  print('Sua expressão está errada!')
 #cada vez que um ( é colocado na lista , ela fica maior que 0, para cada parentes ) ele encontra seu par e
# o remove da lista, entao se tiver dois (( e um ), ele vai remover o seu correspondente, e assim a lista continua com um ,
# fazendo a expressão ser invalida.