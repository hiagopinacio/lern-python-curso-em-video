from time import sleep
from random import randint


def jokenpo():
    itens = ('PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO', 'SPOCK')
    computador = randint(0, 5)
    print('{:=^40}'.format(' VAMOS JOGAR JOKENPO!!! '))
    print('''Sua opções
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
    [ 3 ] Lagarto
    [ 4 ] Spock
    [ 5 ] Regras
    [>=6] Sair''')

    jogador = int(input('Sua opção é?: '))

    if jogador >= 6:
        print('BYE BYE!!')
        exit()

    else:
        if jogador == 5:
            print('PEDRA')
            sleep(1)
            print('PAPEL')
            sleep(1)
            print('TESOURA')
            sleep(1)
            print('LAGARTO')
            sleep(1)
            print('REGRAS!!!')

            print(''' O jogo de pedra, papel, tesoura, lagarto e spock funciona assim
        
                Tesoura corta papel 
        
                Papel cobre pedra 
        
                Pedra esmaga lagarto 
        
                Lagarto envenena Spock 
        
                Spock esmaga (ou derrete) tesoura
        
                Tesoura decapita lagarto 
        
                Lagarto come papel 
        
                Papel refuta Spock 
        
                Spock vaporiza pedra 
        
                Pedra quebra tesoura''')

            jogador = int(input('Sua opção é?: '))

        print('PEDRA')
        sleep(1)
        print('PAPEL')
        sleep(1)
        print('TESOURA')
        sleep(1)
        print('LAGARTO')
        sleep(1)
        print('SPOCK')

        print('<==>' * 10)
        print('O computador escolheu {}!'.format(itens[computador]))
        print('O jogador escolheu {}!'.format(itens[jogador]))
        print('<==>' * 10)

        if computador == 0:  # PEDRA
            if jogador == 0:
                print('EMPATE')

            elif jogador == 1:
                print('JOGADOR VENCEU')

            elif jogador == 2:
                print('''COMPUTADOR VENCEU
                    \033[4;31mGAME OVER\033[m''')

            elif jogador == 3:
                print('''COMPUTADOR VENCEU
                    \033[4;31mGAME OVER\033[m''')

            elif jogador == 4:
                print('JOGADOR VENCEU')
            jokenpo()

        elif computador == 1:  # PAPEL

            if jogador == 0:
                print('''COMPUTADOR VENCEU
                    \033[4;31mGAME OVER\033[m''')

            elif jogador == 1:
                print('EMPATE')

            elif jogador == 2:
                print('JOGADOR VENCEU')

            elif jogador == 3:
                print('JOGADOR VENCEU')

            elif jogador == 4:
                print('''COMPUTADOR VENCEU
                    \033[4;31mGAME OVER\033[m''')
            jokenpo()

        elif computador == 2:  # TESOURA

            if jogador == 0:
                print('JOGADOR VENCEU')

            elif jogador == 1:
                print('''COMPUTADOR VENCEU
                \033[4;31mGAME OVER\033[m	''')

            elif jogador == 2:
                print('EMPATE')

            elif jogador == 3:
                print('''COMPUTADOR VENCEU
                    \033[4;31mGAME OVER\033[m''')

            elif jogador == 4:
                print('JOGADOR VENCEU')
            jokenpo()

        elif computador == 3:  # LAGARTO

            if jogador == 0:
                print('''COMPUTADOR VENCEU
                    \033[4;31mGAME OVER\033[m''')

            elif jogador == 1:
                print('''COMPUTADOR VENCEU
                    \033[4;31mGAME OVER\033[m''')

            elif jogador == 2:
                print('JOGADOR VENCEU')

            elif jogador == 3:
                print('EMPATE')

            elif jogador == 4:
                print('JOGADOR VENCEU')
            jokenpo()

        elif computador == 4:  # SPOCK

            if jogador == 0:
                print('''COMPUTADOR VENCEU
                    \033[4;31mGAME OVER\033[m''')

            elif jogador == 1:
                print('JOGADOR VENCEU')

            elif jogador == 2:
                print('''COMPUTADOR VENCEU
                \033[4;31mGAME OVER\033[m	''')

            elif jogador == 3:
                print('JOGADOR VENCEU')

            elif jogador == 4:
                print('EMPATE')
            jokenpo()
jokenpo()
