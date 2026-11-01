def euclidesMCD(a,b):
    if b ==0:
        return a
    else:
        return euclidesMCD(b, a % b)

print(euclidesMCD(48, 18))