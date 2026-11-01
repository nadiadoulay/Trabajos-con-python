def sumaDigitos (n):
    if n < 10:
        return n
    else:
        return n % 10 + sumaDigitos(n//10)

print(sumaDigitos(1234))