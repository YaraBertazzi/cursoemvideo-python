# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
  """
  ->Calcule o Fatorial de um número.
  :para n: O numero a ser calculado
  :para show: (OPCIONAL) Mostra ou não a conta.
  :return: Valor do fatorial n
  """
  f = 1
  for c in range(n, 0, -1): #começando do zero até o n , voltando um (-1)
    if show:
      print(c, end='')
      if c > 1: # se o c for maior que um
        print(' x ', end='')
      else:
        print(' = ', end='')
    f *= c
  return f


#PROGRAMA PRINCIPAL
#print(fatorial(5, show=True))
help(fatorial)