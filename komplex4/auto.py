class Auto:
    def __init__(self,s):
        sor=s.split(";")
        self.rendszam = sor[0]
        self.marka = sor[1]
        self.szin = sor[2]
        self.gyev = int(sor[3])
lista=[]
with open("auto.txt","r",encoding="UTF-8") as f:
    for i in f:
        lista.append(Auto(i.strip()))
f.close()

print(f"{len(lista)}db auto van")

ki=open("ki.txt", "w", encoding="UTF-8")
for i in lista:
    ki.write(i.marka+"\n")
ki.close()

for i in lista:
    if i.rendszam[0]==i.rendszam[1]==i.rendszam[2] or i.rendszam[3]==i.rendszam[4]==i.rendszam[5]:
        print(i.rendszam)

a=input("marka: ")
db=0
for i in lista:
    if i.marka==a:
        db+=1
        print(f"a kereskedesben {db} db {a}van")
        print(f"{2023-i.gyev}")
