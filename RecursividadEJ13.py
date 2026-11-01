def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)


def mcm(a, b):
    return (a * b) // mcd(a, b)


print(mcm(4, 6))