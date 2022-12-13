from operator import index
import random
import math
"""
x=[]
lista=[]
a=int(input("viz aktualis allasa 100-200cm kozott:"))
amas=[a]
if 99<a<201:
    for i in range (0,20):
        x.append(random.randint(1,10))
        if a<149:
            print(f"{amas+x}")
print(lista)
print(x)
"""

lista=[]
x=[]
a=lista
for i in range(20):
    y=random.randint(100,200)
    x=random.randint(0,11)
    if y<150:
        y=y+x
        lista.append(y)
    else:
        lista.append(y)

print(lista.index(max(lista)))
print(lista.index(min(lista)))
print(sum(lista)/len(lista))


