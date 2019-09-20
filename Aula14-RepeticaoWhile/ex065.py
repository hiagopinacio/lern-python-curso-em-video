# calcular media, maior e menor

# primeira iteração
n = float(input('numero: '))
soma = maior = menor = n
cont = 1
run = str(input('continuar? [s/n]')).strip().lower()

while run not in 'sn':
    run = str(input('digite um valor válido continuar? [s/n]')).strip().lower()

# REPETIÇÃO
while run == 's':
    n = float(input('numero: '))
    soma += n
    cont += 1

    if n > maior:
        maior = n

    if n < menor:
        menor = n

    run = str(input('continuar? [s/n]')).strip().lower()
    while run not in 'sn':
        run = str(input('Digite um valor válido! continuar? [s/n]')).strip().lower()

# RESULTADOS
print("""
    MÉDIA: {}
    MAIOR: {}
    MENOR: {}""".format(soma / cont, maior, menor))
