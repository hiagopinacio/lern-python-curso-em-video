def leiaDinheiro():
    din = str(input("Digite o valor: R$ "))
    din = din.replace(',', '.').strip()
    return float(din)
