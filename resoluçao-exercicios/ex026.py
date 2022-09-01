frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezez na frase.'.format(frase.count('A'))) #encontra o parametro que esta dentro de () na frase
print('A primeira letra A, apareceu na posição {}'.format(frase.find('A')+1)) #a primeira posição começa em zero , ao colocar +1 ele coloca como se tivesse começado por 1
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))   #ultima posição da direita para esquerda
