a=int(input("szam: "))
lista=[]
prim=[]
nem=[]
while a>0:
    a=int(input("szam: "))
    lista.append(a)

def prim_e(x):
    db=0
    for i in range(1, x+1):
        if x%i==0:
            db += 1
    if db == 2:
        return True
    else:
        return False
for i in lista:   
        if prim_e(i)==True:
            prim.append(i)
        elif prim_e(i)==False:
            nem.append(i)

print(f"Primszamok:{prim}")
print(f"Nem primszamok:{nem}")
for i in lista:
    if prim_e(i)==True:
        print(f"legnagyobb prim szam{max(prim)}")
print(f"az osszes atlaga: {sum(lista)/len(lista)}")
