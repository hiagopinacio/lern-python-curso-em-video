#VERIFICAR SE OS PARENTESES DE UMA EXPRESSÃO ESTÃO CORRETOS
exp = str(input('digite uma expressão: '))

if exp.count('(') != exp.count(')'):
    print('expressão inválida')
    correta = False
else:
    for pos, valor in enumerate(exp):
        if exp[:pos].count(')') > exp[:pos].count('('):
            print('expressão inválida')
            correta = False
            break
        else:
            correta = True

if correta:
    print('expressão correta')