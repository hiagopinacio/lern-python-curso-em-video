# verificar quantos "A", qual a posição do primeiro e do ultimo "A"

nome = str(input('digite um nome\n')).strip().upper()

print('o nome tem {} "A"'.format(nome.count("A") ))
print('a primeira letra está na posição {}'.format(nome.find('A')+1) )
print('a útima letra está na posição {}'.format(nome.rfind('A')+1) )