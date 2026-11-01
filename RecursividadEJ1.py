def sucesion (n:int)-> int:
    if n == 0:
        return 1
    elif n ==1:
        return 2
    else:
        return sucesion (n-1) + sucesion (n-2)
print (sucesion (5))