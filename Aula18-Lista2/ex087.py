m = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        m[i].append(float(input(f'digite o valor para [{i}, {j}]: ')))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {m[i][j]:^5} ]', end=' ')
    print()

somapares = 0
for i in range(0, 3):
    for j in range(0, 3):
        if m[i][j] % 2 == 0:
            somapares += m[i][j]
print(f'Soma dos pares = {somapares}')

somacol3 = 0
for i in range(0, 3):
    somacol3 += m[i][2]
print(f'Soma da coluna 3 = {somacol3}')

print(f'O maior valor da segunda linha é {max(m[1])}')

