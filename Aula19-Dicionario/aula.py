filme = dict()
filme = {'titulo': 'Matrix', 'ano': 1999}
print('lista:', filme)
print('atributo titulo:', filme['titulo'])
print('atributo ano:', filme['ano'])

# adicionando parametros a
print('\nadicionando chave diretor e volume')
filme['diretor'] = 'Wachowski'
filme['volume'] = 1
print(filme)

# deletando parâmetros
print('\ndeletando chave volume')
del filme['volume']
print(filme)

# Pegando chaves e valores
print('\nfunções de dicionarios')
print('pegando valores:', filme.values())
print('pegando chaves:', filme.keys())
print('pegando chave e valores:', filme.items())

# utilização do FOR
print('\nmostrar dicionario utilizando for')
for k, v in filme.items():
    print(f'    o {k} é {v}')

# CRIANDO LISTA DE DICIONÁRIOS
print('\nlista de filmes')
filme2 = {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}
filme3 = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
locadora = list()
locadora = [filme, filme2, filme3]
print(locadora)
print('ano do filme na posição 0 da lista:', locadora[0]['ano'])
print('titulo do elemento 2:', locadora[2]['titulo'])

# COPIANDO DICIONÁRIOS
print('\nCÓPIA')
filme4 = filme3
filme3['ano'] = 2018

print('copiando um dicionario e mudando o ano:', filme3)
print('cópia altera também', filme4)

filme4 = filme3.copy()
filme3['ano'] = 1977
print('utilizando método copy:')
locadora.append(filme4)
for v in locadora:
    print(v)

# MOSTRANDO VALORES COM FOR ANINHADO
print('\n\n-=-= Mostrando valores com for aninhado =-=-\n')
for i in locadora:
    for v in i.values():
        print(v, end=', ')
    print()

# ORDENAR DICIONÁRIO
print('\n\n-=-= ordenando dicionarios =-=-\n')
from operator import itemgetter

datado = sorted(locadora, key=itemgetter('ano')) #utilizando a importação
datado = sorted(locadora, key=lambda x: x['ano']) #utilizando função anônima; cada item da lista será devolvido o ano do item
print('em ordem de datas:')
for v in datado:
    print(v)
dicionario = {'n1': 5, 'n2': 1, 'n3': 4, 'n4': 10}
print('\ndicionario considerado:', dicionario)
ordenado = sorted(dicionario.items(), key=lambda x: x[1], reverse=True)
ordenado = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print(ordenado)
