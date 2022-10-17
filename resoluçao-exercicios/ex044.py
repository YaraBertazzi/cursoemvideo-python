produto = float(input('Digite o valor do Produto: R$ '))
pagamento = int(input('Digite a opção de pagamento: \n 1 - A vista/cheque \n 2 - Á vista no cartão \n'
                      ' 3 - Em até 2x no cartão \n 4 - Em até 3x no cartão '))
#1- 10%  , 2- 5% , 3- preço normal, 20% de juros
if pagamento == 1 :
    desc = produto - ((produto * 10) / 100)
    print(f'Com desconto de 10% , valor do pagamento do produto é  R$ {desc}')
elif pagamento == 2 :
    desc1 = produto - ((produto * 5) / 100)
    print(f'Com desconto de 5% , valor do pagamento do produto é  R$ {desc1}')
elif pagamento == 3 :
    print(f'Valor do pagamento do produto é R$ {produto}')
elif pagamento == 4 :
    juros =  produto + ((produto * 20) / 100)
    print(f'O parcelamento mais o juros de 20%, o valor do produto é R$ {juros}')


