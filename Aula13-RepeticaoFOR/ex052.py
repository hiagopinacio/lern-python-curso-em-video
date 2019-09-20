n = 29

c = 0
for x in range(2, int(n/2)+1):
    if n % x == 0:
        c += 1
        print('{} dividido por {} é igual a {}'.format(n, x, n / x))
if c != 0:
    print('{} não é primo'.format(n))
else:
    print('{} é primo'.format(n))
