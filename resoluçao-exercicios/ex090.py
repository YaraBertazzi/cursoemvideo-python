aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
  aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['média'] <7:
  aluno['situacao'] = 'Recuperação'
else:
  aluno['situacao'] = 'Reprovado'
print('-='*20)
for k, v in aluno.items():
  print(f' - {k} é igual a {v}')
