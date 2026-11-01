def binario (n):
    if n < 2:
        return n
    else:
        return binario(n // 2) * 10 + (n % 2)
    
print(binario(4))