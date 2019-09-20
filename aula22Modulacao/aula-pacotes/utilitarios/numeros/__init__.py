def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


if __name__ == '__main__':
    n = int(input("digite um número: "))
    print(f'{n}! = {fatorial(n)}')