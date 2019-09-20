def aumentar(n, v, formatar=True, m='R$'):
    r = n * (1 + v / 100)
    if formatar:
        return moeda(r, m)
    else:
        return r


def diminuir(n, v, formatar=True, m='R$'):
    r = n * (1 - v / 100)
    if formatar:
        return moeda(r, m)
    else:
        return r


def dobro(n, formatar=True, m='R$'):
    r = n * 2
    if formatar:
        return moeda(r, m)
    else:
        return r


def metade(n, formatar=True, m='R$'):
    r = n / 2
    if formatar:
        return moeda(r, m)
    else:
        return r


def moeda(n, m='R$'):
    return f'{m} {n:.2f}'.replace('.', ',')


def resumo(p, aum, red):
    print('*'*30)
    print(f'{"Resumo do Valor":^30}')
    print('*'*30)
    print(f'{"Valor Analisado":.<20}{moeda(p):.>10}')
    print(f'{"Dobro do valor":.<20}{dobro(p):.>10}')
    print(f'{"metade do valor":.<20}{metade(p):.>10}')
    print(f'{aum:.2f}% {"de aumento":.<13}{aumentar(p,aum):.>10}')
    print(f'{red:.2f}% {"de redução":.<13}{diminuir(p,red):.>10}')
    print('*'*30)
