import moeda

n = float(input('digite um valor: R$ '))
print(f'O dobro de {n} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {n} é {moeda.moeda(moeda.metade(n))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Diminuindo 10% temos {moeda.moeda(moeda.diminuir(n, 10))}')
