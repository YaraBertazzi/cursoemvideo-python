n = str(input('Digite seu nome completo:')).strip()
nome = n.split()  #separa por espaços
print('Seu primeiro nome é: {}'.format(nome[0])) 3posição do primeiro nome
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1])) #acha aposição do ultimo nome , independnete do tamanho com o -1
