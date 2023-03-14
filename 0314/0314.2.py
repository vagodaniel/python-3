class Verseny():
    def __init__(self,s):
        sor=s.split("\t")
        self.nev=sor[0]
        self.datum=sor[1]
        self.nemzetiseg=sor[2]
        self.rajtszam=int(sor[3])
lista=[]
with open("versenyzok.txt", "r", encoding="utf-8") as f:
    f.readline()
    for i in f:
        lista.append(Verseny(i.strip()))

# Hány versenyző van?
print(len(lista))
#Hány német versenyző van?
db=0
for i in lista:
    if i.nemzetiseg=="német":
        db+=1
print(db)
#Milyen nemzetiségű versenyzők vannak a fájlban?
nemzet=[]
for i in lista:
    if i.nemzetiseg in nemzet:
        continue
    else:
        nemzet.append(i.nemzetiseg)
print(nemzet)
#Nemzetiség szerint hány versenyző indult?
nemzetek=[]
for i in lista:
    nemzetek.append(i.nemzetiseg)
print(set(nemzetek))

#hazi: nobel.txt