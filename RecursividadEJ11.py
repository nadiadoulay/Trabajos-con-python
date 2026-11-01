def invertir (n:int, resultado=0) -> int:
    if n == 0:
        return resultado
    else:
        ultimo = n % 10
    resultado = resultado * 10 + ultimo

    return invertir(n // 10, resultado)


print(invertir(1234))