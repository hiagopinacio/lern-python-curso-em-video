valor = int(input('valor sacado: R$'))

n50=valor//50
resto = valor-50*n50
n20 = resto//20
resto = resto-20*n20
n10 = resto//10
n1 = resto-10*n10

print(f"""
Notas de 50: {n50}
Notas de 20: {n20}
Notas de 10: {n10}
Notas de 1: {n1}""")
