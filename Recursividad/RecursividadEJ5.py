def romano_a_decimal(texto):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100
    }

    total = 0

    for i in range(len(texto)):
        actual = valores[texto[i]]

        if i < len(texto) - 1:
            siguiente = valores[texto[i+1]]

            if actual < siguiente:
                total -= actual
            else:
                total += actual
        else:
            total += actual

    return total


print(romano_a_decimal("XIV"))
