salario = float(input('Digite seu salário: '))
if salario > 1250.00:
    aumento = (salario* 10 /100) + salario
    print('Seu salário de {:.2f} R$ teve um aumento de 10%, agora é {:.2f} R$'.format(salario,aumento))
else:
    a = (salario * 15 / 100) + salario
    print('Seu salário de {:.2f} R$ teve um aumento de 15%, agora é {:.2f} R$'.format(salario,a))