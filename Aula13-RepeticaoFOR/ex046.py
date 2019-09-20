# contagem regressiva de 10 a 0
from time import sleep

print('contagem regressiva iniciada')

for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('BUMMM!')
