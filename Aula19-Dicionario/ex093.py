jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))

n = int(input(f'Número de partidas jogadas por {jogador["nome"]}: '))
jogador['gols'] = []
for i in range (0, n):
    jogador['gols'].append(int(input(f'Gols marcados na {i+1}ª partida: ')))
jogador['total de gols'] = sum(jogador['gols'])

print('\n' + '*'*50)

print(jogador)

print('\n' + '*'*50)

for k, v in jogador.items():
    print(f'campo {k} tem o valor {v};')

print('\n' + '*'*50)
print(f'{jogador["nome"]} jogous {len(jogador["gols"])} partidas')
for i, g in enumerate(jogador['gols']):
    print(f'    =>na {i+1}ª partida, marcou {g} gols')
print('TOTAL DE GOLS =', jogador['total de gols'])