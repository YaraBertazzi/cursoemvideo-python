lista = [[], []]  # dentro de uma lista , tem outras duas listas
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}° numero: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-=' * 30)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores imapres digitados foram: {lista[1]}')