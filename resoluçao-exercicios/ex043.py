alt = float(input('Digite sua altura em cm: '))
peso = float(input('Digite sei peso: '))
imc = peso / (alt /100 )**2
print(f'imc é: {imc:.2f}')

if imc < 18.5 :
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25.0 :
    print('Peso ideal')
elif imc >= 25.0 and imc < 30.0 :
    print('Sobrepeso')
elif imc >= 30.0 and imc < 40.0 :
    print('Obesidade')
elif imc > 40.0 :
    print('Obesidade Mórbita')