import moeda

n = float(input('digite um valor: R$ '))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, False)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n)}')
print(f'Aumentando 10% temos {moeda.aumentar(n, 10)}')
print(f'Diminuindo 10% temos {moeda.diminuir(n, 10)}')
