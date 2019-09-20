# verificar se o nome da cidade começa com a palavra Santo

nome = str(input('digite o nome da cidade\n')).strip()
nome5=nome[:5].capitalize()
print(nome5)
print('nome da cidade começa com Santo? {}'.format('Santo' in nome[:5].capitalize()))
