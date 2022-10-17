palavras = (
'aprender', 'programar', 'linguagem', 'pyhton', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
'programador', 'futuro')
# tupla de palavras , e cada palavra é como um lista
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
