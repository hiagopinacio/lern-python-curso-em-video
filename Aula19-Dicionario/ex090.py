aluno = {}
aluno['nome'] = 'Hiago'
aluno['média'] = 97

if aluno['média'] >= 70:
    aluno['situacao'] = 'APROVADO'
elif aluno [ 'média'] < 50:
    aluno['situacao'] = 'REPROVADO'
else:
    aluno['situacao'] = 'de RECUPERAÇÃO'

print(f' O aluno {aluno["nome"]} está {aluno["situacao"]} com média {aluno["média"]}')