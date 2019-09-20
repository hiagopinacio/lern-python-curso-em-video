def notas(*notas, sit=False):
    '''
    Verifica a situação da turma
    :param notas: todas as notas da turma
    :param sit: mostrar a situação, default é False
    :return: dicionário com: o total de notas, a menor nota, a maior nota, a média das notas e a situação se sit=True
    '''
    resp = dict()
    resp['quatidade'] = len(notas)
    resp['menor'] = min(notas)
    resp['maior'] = max(notas)
    resp['média'] = sum(notas)/len(notas)
    if sit:
        if resp['média'] >=7:
            resp['situação'] = 'BOA'
        elif resp['média'] < 5:
            resp['situação'] = 'RUIM'
        else:
            resp['situação'] = 'RAZOAVEL'
    return resp


print(notas(5.3, 5.4, 2, 6, 8.5, 0, 7.3, sit=True))
help(notas)
