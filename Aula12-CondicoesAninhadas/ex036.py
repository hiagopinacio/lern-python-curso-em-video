#financiar casa se a parcela for menor que 30% do salário

v = float(input('valor da casa: '))
s = float(input('seu salário: '))
n = int(input('anos para pagar: '))

p = v/n/12 #valor da parcela

if p<=s*0.3:
    print('a prestação mensal será R${:.2f}'.format(p))
else:
    print('para este financiamento você deveria receber pelo menos R${:.2f} por mês'.format(p/0.3))