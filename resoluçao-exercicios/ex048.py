soma = 0  # acumulador de numero
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
print(soma)
