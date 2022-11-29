from itertools import count
import random
from traceback import print_list
"""
lista=[]
for i in range (12):
    lista.append(random.randint(-20,20))
print(lista)
print(max(lista)-min(lista))
"""
"""
lista1=[]
for i in range (10):
    lista1.append(random.randint(0,100))
db=0
for elem in lista1:
    if elem %2==0:
        db+=1
print(lista1)
print(db)

print(max(lista1))
print(sorted(lista1)[-2])
"""
"""
osszeg=0
nap=0
while osszeg<=100:
    km=int(input("kilometer:"))
    osszeg+=km
    nap+=1
print("grat elerted")
print(f"{osszeg-100} km-el jobb vagy,mint aki 100-at csinalt")
print(f"a turat {nap} nap alatt tetted meg")
"""
"""
nevek=[]

for i in range(10):
    nevek.append(input("neve.k:"))
print(nevek)
space=0
db=[]
for nev in nevek:
    space=0
    for betu in nev:
        if betu==" ":
            space+=1
    if space==2:
        db.append(nev)
print(len(db))

hossz=[]
for nev in nevek:
    hossz.append(len(nev))
maxhossz=max(hossz)
for nev in nevek:
    if len(nev)==maxhossz:
        print(nev)
"""

verseny=[]
print("adj meg egy nevet es hogy hany km-t futott")
for i in range(5):
    verseny.append((input(),int(input())))
print(verseny)
print(verseny[1][0])
km=[verseny[0][1]]
for i in range (len(verseny)-1):
    km.append(verseny[i+1][1]-verseny[i][1])
print(km)
maxkm=max(km)
maxii=0
for i in range(len(km)):
    if km[i]==maxkm:
        maxii=i
print(verseny[maxii])
print(maxkm)