def raiz(n):
    return auxiliar(n, 1)


def auxiliar(n, x):
    if x * x > n:
        return x - 1
    return auxiliar(n, x + 1)


print(raiz(10))