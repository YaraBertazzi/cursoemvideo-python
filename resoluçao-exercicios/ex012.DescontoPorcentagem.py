#Faca um algoritimo que leia o preco de um produto e depois mostre seu novo preço com desconto de 5 %
p = float(input('Valor de um produto:'))
novo = p - (p / 100 * 5)
print('O valor a ser pago do produto com 5% de desconto é {}'.format(novo))
