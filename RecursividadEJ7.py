def algoritmo (n:int)-> int:
    if n == 1:
        return 1
    else:
       return 1/n + algoritmo(n-1)

print(algoritmo(5))