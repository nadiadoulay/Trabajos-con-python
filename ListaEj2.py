from random import choice
from list_ import List

l=List()

letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
size=0
for i in range(50):
    l.append(choice(letras))

l.show()
size = l.size()

for i in range(size):
    l.delete_value("A")
    l.delete_value("E")
    l.delete_value("I")
    l.delete_value("O")
    l.delete_value("U")

print ("Lista sin vocales: ")
l.show()
       
   

