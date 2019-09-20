from datetime import date

pessoa = {}
pessoa['nome'] = str(input('Digite o nome: '))
pessoa['nascimento'] = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - pessoa['nascimento']
carteira = int(input('Carteira de trabalho: '))
if carteira != 0:
    pessoa['ctps'] = carteira
    pessoa['ano de contrato'] = int(input('ano de contrato: '))
    pessoa['ano de aposentadoria'] = pessoa['ano de contrato'] + 35
    pessoa['tempo para aposentar'] = pessoa['ano de aposentadoria'] - date.today().year
    pessoa['idade de aposentadoria'] = pessoa['ano de aposentadoria'] - pessoa['nascimento']
print('\n' + '-=-'*10)
for k, v in pessoa.items():
    print(f'{k} é {v}')
print(pessoa)
