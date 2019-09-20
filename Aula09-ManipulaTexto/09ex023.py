#mostrar unidades, centenas, dezenas e milhares de um numero de 0 a 9999

n=int(input('digite um número inteiro de 0 a 9999\n').strip())
u=n%10
d=n//10%10
c=n//100%10
m=n//1000%10

print('unidades: {}'.format(u))
print('dezenas: {}'.format(d))
print('centenas: {}'.format(c))
print('milhares: {}'.format(m))