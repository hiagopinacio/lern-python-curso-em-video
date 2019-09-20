import moeda

n = float(input('digite um valor: R$ '))
print(f'O dobro de {n} é R$ {moeda.dobro(n)}')
print(f'A metade de {n} é R$ {moeda.metade(n)}')
print(f'Aumentando 10% temos R$ {moeda.aumentar(n, 10)}')
print(f'Diminuindo 10% temos R$ {moeda.diminuir(n, 10)}')
