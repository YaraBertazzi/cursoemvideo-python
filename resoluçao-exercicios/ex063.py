print('_'*30)
print('Sequência de Fibonacci')
print('_'*30)
n = int(input('Quantos termos quer mostrar? '))
t1 = 0 #primeiro termo
t2 = 1 #segundo termo
print('{} -> {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3),end='')
    '''conforme vai avancando o t1 passa a ser o t2 , o t2 passa aser o proximo, eo t3 passa a ser a soma 
    0 -> 1 -> 1 -> 2 -> 3 ->
                   t1   t2   t3'''
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')
