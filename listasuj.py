"""
from audioop import reverse
from csv import list_dialects
import random 
lista=[]
for i in range(10):
    lista.append(random.randint(1,1000))
print(lista)
print(sum(lista)/len(lista))
for i in lista:
    if i%11==0 and i<100 or i%111==0:
        print(i)
       
db=0
for i in lista:
    if i>9 and i<100:
        db+=1
print(db)
print(len([x for x in lista if x>9 and x<100]))
print([x**2 for x in lista if x<10])
print(sum([x for x in lista if x%3==0]))
print(len([x for x in lista if x%3==0]))
print([x for x in lista if x%3==0])
print(len([x for x in lista if x%10==0]))
print(max([x for x in lista if x%5==0]))
print(len([x for x in lista if x>500 and x<1000]))
print(sum([x for x in lista if x<10]))

print(sorted([x for x in lista if x%3==0])[::-1])


lista.insert(4,50)
print(len(lista))
print(lista.index(50))
print(lista.count(50))
print(lista.remove(50))
print(lista[::-1])
print(lista[2:8:2])
print(lista[-3:-8:-1])


mondat=input("kerek mondat:")
print(mondat.count(" ")+1)
print(len(mondat))
mgh=["a","á","e","é", "i"]
db=0 
for i in mondat:
    if i in mgh:
        db+1
        print(db)

"""
mondat=input("mondatod:")
szo=input("szo:")
ind=mondat.index(" ")
elso=mondat[:ind+1]+szo
mosod=mondat[ind:]
print(elso + mosod)