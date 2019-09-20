def soma2(a, b):
    s = a + b
    print(f'a = {a}; b = {b}; a + b = {s}')


soma2(3, 4)
soma2(b=3, a=4)


# ==================================================
# EMPACOTAMENTO NO PYTHON (foda)
# ==================================================
def soma(*num):
    print(f'soma de {num} = {sum(num)}')


soma(3, 5, 1, 6, 7)


# ==================================================
# PARAMETROS OPCIONAIS & DOCUMENTAÇÃO
# ==================================================

def soma3(a=0, b=0, c=0):
    """
    Soma até 3 valores.
    Parâmetros opcionais:
    :param a: valor a, default is 0.
    :param b: valor b, default is 0.
    :param c: valor c, default is 0
    :return: soma = a+b+c
    """
    soma = a + b + c
    return soma


print(soma3(1, 2))
print()
help(soma3)

# ==================================================
# VARIÁVEIS GLOBAIS DENTRO DE FUNÇÃO
# ==================================================


def teste():
    global a
    a = 5
    print(f'a na função vale {a}')


a = 2
teste()
print(f'a global vale {a}')
