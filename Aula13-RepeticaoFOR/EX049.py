#tabuada

n = int(input('digite um numero: '))

for c in range (0, 11):
    print('{} x {:>2} = {}'. format(n,c,n*c))
