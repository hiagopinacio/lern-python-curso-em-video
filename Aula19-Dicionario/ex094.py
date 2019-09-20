lista = []
pessoa = {}
continua = 'S'
soma = 0
while continua == 'S':
    pessoa['nome'] = str(input(f'{"Nome: ":>10}'))

    while True:
        pessoa['sexo'] = str(input(f'{"Sexo: ":>10}')).strip().upper()
        if pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
            print('\033[1;31mdigite um valor válido [f/m]\033[m')
        else:
            break

    pessoa['idade'] = int(input(f'{"idade: ":>10}'))
    soma += pessoa['idade']
    continua: str = input('deseja continuar? ').strip().upper()

    while continua != 'N' and continua != 'S':
            print('\033[1;31mdigite um valor válido [s/n]\033[m')
            continua = input('deseja continuar? ').strip().upper()

    lista.append(pessoa.copy())

media = soma/len(lista)
mulheres = []
velhos = []
for v in lista:
    if v['sexo'] == 'F':
        mulheres.append(v['nome'])
    if v['idade'] > media:
        velhos.append([v['nome'], v['idade']])

print(f'\033[36mForam cadastradas {len(lista)} pessoas')
print(f'a média de idade é {media}')
print('mulheres cadastradas: ', end='')
for v in mulheres:
    print(v, end=', ')
print()
print('pessoas mais velhas: ', end='')
for v in velhos:
    print(f'{v[0]} com {v[1]} anos, ', end='')


