cont = ('zero', 'um', 'dois', 'tres', 'quatro',
       'cinco', 'seis', 'sete', 'oito',
       'nove', 'dez', 'onze', 'doze', 'treze', 'quatroze',
       'quinze', 'dezesseis', 'dezzesete', 'dezoito', 'dezenove', 'vinte')
while True:
       n = int(input('Digite um número entre 0 a 20: '))
       if 0 <= n <=20:
              break
       print('Tente novamente.', end='')
print(f'Voce digitou o número {cont[n]}')
