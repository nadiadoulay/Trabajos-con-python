from random import randint
from list_ import List

l=List()
pares=List()
impares=List()

for i in range(20):
    l.append(randint(1,100))

while l.size()>0:
    num = l.pop()
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)

print("Pares: ")
pares.show()
print("Impares: ")
impares.show()