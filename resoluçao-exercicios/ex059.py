n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print('''  [ 1 ] somar
  [ 2 ] multiplicar 
  [ 3 ] maior 
  [ 4 ] novos números 
  [ 5 ] sair do programa ''')
    opcao = int(input('Qual a sua opção?'))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, soma))

    elif opcao == 2 :
        mult = n1 * n2
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, mult))

    elif opcao == 3:
        # if n1 > n2:
        # maior = n1
        # else:
        maior = n2
        print('Entre {} e {} i maior valor é {}'.format(n1, n2, maior))

    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))

    elif opcao == 5:
        print('Opção')

    else:
        print('Opção invalida. Tente novamene')
        print('=-' * 20)
        print('Fim do programa! Volte sempre')

