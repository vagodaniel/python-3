"""
class Csoport():#osztály létrehozása
    def __init__(self, s): #konstruktor – alapbeállítás - inicializáló függvény
        sor=s.split(";") #szétbontjuk a sort a szeparátorjel mentén mezőkre
        self.nev=sor[0]
        self.mag=int(sor[1])

lista=[]
with open("csoport.txt","r",encoding="utf-8") as f:
    for i in f:
        lista.append(Csoport(i.strip()))
f.close()
print(lista[0].nev)
"""

"""
lista=[]
f=open("gyumi.txt","r",encoding="UTF-8")
"""

"""
for sor in f:
    lista.append(sor.strip())
f.close()
print(lista)
"""
"""
lista=f.readlines()
print(lista)
uj=[]
for i in lista:
    uj.append(i.strip())
print(uj)
"""
"""
ki=open("csillag.txt", "w", encoding="UTF-8")
dbE=0
dbe=0

while True:
    betu=f.read(1)
    if betu:
        if betu=="E" or betu=="e":
            print("*",end="")
            if betu=="E":
                 dbE+=1
            elif betu=="e":
                 dbe+=1
        else:
            print(betu,end="")
    else:
        break
f.close()
ki.close()
print(f"E betuk szama: {dbE}, e betuk szama: {dbe}")
"""
"""
class Csoport():
    def __init__(self,s):
        sor=s.split(";")
        self.nev=sor[0]
        self.magassag=int(sor[1])
lista=[]
with open("csoport.txt","r", encoding="UTF-8") as f:
    for i in f:
        lista.append(Csoport(i.strip()))
f.close()
for i in lista:
    print(f"{i.nev} - {i.magassag}")
osszeg=0
for i in lista:
    osszeg+=i.magassag
atlag=round(osszeg/len(lista),2)
print(atlag)
max_mag=lista[0].mag
maxi=0
for i in range(len(lista)):
    if max_mag<lista[i].mag:
    max_mag=lista[i].mag

maxi=i

print(f"legmagasabb: {lista[maxi].nev} magassága: {max_mag}")
"""
"""
class Eu():
    def __init__(self,s):
        sor=s.split(";")
        self.orszag=sor[0]
        self.ev=int(sor[1])
        
lista=[]


with open("eu.txt","r", encoding="UTF-8") as f:
    for i in f:
        lista.append(Eu(i.strip()))
f.close()

#azpl az orszagok amibe benen van az orszag szo
for i in lista:
    if "orszag" in i.orszag:
        print(i.orszag)

#szerepel e mo az orszagok kozott
van=False
for i in lista:
    if "Magyarország" in i.orszag:
        print(van)
        van=True
    else:
        print("nincs")
"""


#csv beolvasas

class Eu():
    def __init__(self) -> None:
        pass