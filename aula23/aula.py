try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b


# except (ValueError, TypeError ) as e:
#    print(f'Os dados digitados não são válidos\n{e}')

# except ZeroDivisionError as e:
#    print(f'ERRO: {e}')

# except KeyboardInterrupt as e:
#    print(f'ERRO: {e}')###

except Exception as e:  # pega qualquer excessão
    print(f'ERRO: {e}')
else:
    print(f'O resultado é {r}')
finally:  # Sempre executa
    print('FIM')
