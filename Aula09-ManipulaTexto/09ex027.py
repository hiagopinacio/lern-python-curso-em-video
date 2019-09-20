# mostrar primeiro e ultimo nome

nome = str(input('digite um nome\n')).strip().title()
dividido=nome.split()

print('primeiro nome é {}'.format(dividido[0]))
print('ultimo  nome é {}'.format(dividido[len(dividido)-1]))
