from time import sleep


def fatorial(n, show=False):
    if n == 0:
        if show:
            print("0! = ", end='')
        return 1
    elif n>0:
        if show:
            print(f'{n} x ', end='')
            sleep(1)
            s = n*fatorial(n-1, show=True)
        else:
            s = n*fatorial(n-1)
        return s


print(fatorial(0, show=True))