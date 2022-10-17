frase = str(input('Digite uma frase:')).strip().upper() #tira espaços antes e depois (externos) e deixa tudo maiuscula
palavras = frase.split()  #separa
junto = ''.join(palavras) #junta tudo sem espaços internos
inverso = ''
for letra in range(len(junto) -1, -1, -1): #le as letra, -1 ultima letra, ate a primeira letra -1, e elevai voltar (um passo atras -1)
#ele vai começar em len(junto), vai ate a letra -1 que é antes da primeira (0), e vai voltando uma letra
  inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
  print('Temos um palíndromo!')
else:
  print('A frase não é um palíndromo!')
