"""
for i in range(1,11,2):
    print(i, end=" , ")
"""
"""
i=1
while i<11:
    print(i, end=",")
    i+=1
"""
"""
for i in range(1,201,2):
    print(i, end=" , ")
"""
"""
for i in range(3, 50*3, 3 ):
    print(i, end=",")

"""
"""
i=1
while i<151:
    if i%3==0:
        print(i)
    i+=1
"""
"""
for i in range(10,100, 5 ):
    print(i, end=",")
"""
"""
import math
for i in range(1,11):
    print(2**i)
"""
"""
for i in range(1, 6):
    for j in range(1, 6):
        if i==j or i+j==6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""
"""
from operator import truediv


szam=int(input("100 kisebb szam:::"))
prim=True
for i in range(2, szam):
    if szam%i==0:
        prim=False
print("prim" if prim==True else "oszetett")
"""
"""
szam=int(input("Ennek a szamnak az osztoi:"))

for i in range(1, szam+1):
    if szam%i==0:
        print(i)
"""

szam=int(input("100 kisebb szam:::"))
osszeg=0
for oszto in range(1, szam):
    if szam%oszto==0:
        osszeg+=oszto
print("tokeletea" if osszeg==szam else "nem")