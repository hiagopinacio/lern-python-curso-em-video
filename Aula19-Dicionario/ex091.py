from random import randint
from time import sleep

jogadas = {'jogador_1': randint(1, 6),
           'jogador_2': randint(1, 6),
           'jogador_3': randint(1, 6),
           'jogador_4': randint(1, 6)}
for jogador, dado in jogadas.items():
    print(f'{jogador} tirou {dado}')
    sleep(1)

lista= []
for j in jogadas.values():
    lista.append(j)
lista.sort(reverse=True)

print(f'{"RANKING":*^20}')
jogadas_ordem = {}
for n, v in enumerate(lista):
    for jogador, dado in jogadas.items():
        if dado == v:
            jogadas_ordem[jogador] = dado
            del jogadas[jogador]
            break

for jogador, dado in jogadas_ordem.items():
    print(f'1º lugar: {jogador} tirou {dado}')
