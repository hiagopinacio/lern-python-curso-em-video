print(8, 'é do tipo', type(8))  # int
print(8.0, 'é do tipo', type(8.0))  # float
print("'Hiago' é do tipo'", type('Hiago'))  # str
print(True, 'é o tipo', type(True))  # bool

a = input('digite um valor\n')
if a.isnumeric():
    af = float(a)
    ai = int(a)
    if ai == af:
        print('{} é igual a {} em uma expressão condicional'.format(ai, af))
    else:
        print('{} é diferente de {} em uma expressão condicional'.format(ai, af))

# nao consegui verificar quando é digitado um número float
if a.isdecimal():
    print('é decimal')

if a.isalnum():
    print('possui letras e números')

if a.isalpha():
    print('possui apenas letras')

if a.isspace():
    print('possui apenas espaços')
