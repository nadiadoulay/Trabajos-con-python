def producto (a,b: int) -> int:
    if a == 0 or b == 0:
        return 0
    else: 
        return a + producto(a, b-1)

print(producto(3, 4))