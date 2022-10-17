num = []
for n in range(0, 5):
    n = int(input('Digite um número: '))
    num.append(n)
print(f'Você digitou os valores: {num}')
#A- quantas vezes apareceu o numero 9. count (conta)
print(f'O valor 9 apareceu {num.count(9)} vezes')
#B- Em que posição foi digitado o valor 3 index (da posição)
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição.')
else:
  print(f'O valor 3 não foi digitado')
#Quais foram os numeros pares.
print(f'Os valores pares digitados foram ', end=' ')
for n in num:
  if n % 2 ==0:
    print(n, end=' ')