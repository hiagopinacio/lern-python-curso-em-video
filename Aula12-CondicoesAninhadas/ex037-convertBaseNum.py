#convertendo base numérica

n = int(input('digite um número para conversão: '))
b = int(input('escolha a base de conversão\n    1 - binário\n    2 - octal\n    3 - hexadecimal\nEscolha: '))

if b == 1:
    print('binario: {}'.format(bin(n)[2:]))
elif b == 2:
    print('octal: {}'.format(oct(n)[2:]))

elif b == 3:
    print('hexadecimal: {}'.format(hex(n)[2:]))
