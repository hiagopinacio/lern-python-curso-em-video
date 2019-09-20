#código: \033[ Style ; Text ; Background m

#pode colocar apenas os parametros que quiser mudar: [1m ou [1,34m ou [1,33,45m ou [1,4,7,33,45m...
#usar [m vazio para voltar ao normal

#Style: 0 - normal
#       1 - negrito
#       4 - sublinhado
#       7 - negativo (inverte texto e fundo)

#   Text /  Back => Cor:
#   30      40      BRANCO
#   31      41      VERMELHO
#   32      42      VERDE
#   33      43      AMARELO
#   34      44      AZUL
#   35      45      MAGENTA
#   36      46      CYAN
#   37      47      CINZA

print('\033[4;36mOlá, Mundo')
print('\033[1;35;42m {:-^20} \033[m'.format('Mangueira'))

print('\033[1;7;30mInvertendo para escrever preto\033[m' )

print('data: \033[31m{}\033[m de \033[32m{}\033[m de \033[33m{}\033[m'.format('08','janeiro','1993'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m'}

print('meu nome é {}{}{}'.format(cores['azul'], 'Hiago', cores['limpa']))