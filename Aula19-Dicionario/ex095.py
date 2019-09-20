time = []
jogador = {}
continua = 'S'
while continua == 'S':
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))

    n = int(input(f'Número de partidas jogadas por {jogador["nome"]}: '))
    jogador['gols'] = []
    for i in range (0, n):
        jogador['gols'].append(int(input(f'Gols marcados na {i+1}ª partida: ')))
    jogador['total de gols'] = sum(jogador['gols'])

    continua = input('Quer continuar? [s/n]').strip().upper()
    while continua != 'S' and continua != 'N':
        print('\033[1;31mDIGITE UM VALOR VÁLIDO [S/N]\033[m')
        continua = input('Quer continuar (s para sim; n para não)? ').strip().upper()
    time.append(jogador.copy())
    print('\n' + '*'*50)

print(f'  cod {"nome":<20} jogos  gols')
print('-'*40)
for cod, jog in enumerate(time):
    print(f'{cod:>5} {jog["nome"]:<20} {len(jog["gols"]):>5} {jog["total de gols"]:>5}')
print('-'*40)
print('\n' + '*'*50)

while True:
    cod = int(input('mostrar dados do jogador de cod? (999 para sair) ').strip())
    while not (0 <= cod <= len(time)-1):
        cod = int(input(f'\033[1;31mdigite um valor entre 0 e {len(time)-1}: \033[m'))
        if cod == 999:
            break
    if cod == 999:
        break

    print('\n' + '*'*50)
    print(f'{time[cod]["nome"]} jogou {len(time[cod]["gols"])} partidas')
    for i, g in enumerate(time[cod]['gols']):
        print(f'    =>na {i+1}ª partida, marcou {g} gols')
    print('TOTAL DE GOLS =', time[cod]['total de gols'])
    print('\n' + '*'*50)
