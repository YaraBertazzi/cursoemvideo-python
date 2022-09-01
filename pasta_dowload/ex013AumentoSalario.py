#Ler um salario e mostre seu novo salario com 15% de aumento
s = float(input('Salario do funcionario: R$'))
v = s + (s / 100 * 15)
print('Com aumento de 15%, o salário passa a ser {:.2f} R$'.format(v))
