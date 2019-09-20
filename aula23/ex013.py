def leiaint():
    try:
        n = int(input('digite um numero inteiro: '))
        print(f'o valor digitado foi {n}')
        return n
    except KeyboardInterrupt:
        n = 0
        print('\033[1;31mO usuário preferiu não digitar um número!\033[m')
    except Exception as e:
        print('\033[1;31mencontramos um erro:', e)
        print('Digite um número inteiro válido!\033[m')
        leiaint()


def leiafloat():
    try:
        n = float(input('digite um numero real: '))
        print(f'o valor digitado foi {n}')
        return n
    except KeyboardInterrupt:
        n = 0
        print('\033[1;31mO usuário preferiu não digitar um número!\033[m')
    except Exception as e:
        print('\033[1;31mencontramos um erro:', e)
        print('Digite um número real válido!\033[m')
        leiafloat()
    return n


if __name__ == '__main__':
    leiaint()
    leiafloat()
