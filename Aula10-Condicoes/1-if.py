n = 3  # idade do carro
if n < 3:
    print('carro seminovo')
elif n < 5:
    print('carro usado')
else:
    print('carro velho')
print('{:-^20}'.format('FIM'))

# FORMA RESUMIDA

print('carro novo' if n < 3 else 'carro usado ou velho')
