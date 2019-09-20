# soma dos numeros ímpares multiplos de 3 entre 1 e 500

s = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        print('{} + {} = {}'.format(s, c, s + c))
        s += c
print('SOMA FINAL', s)
