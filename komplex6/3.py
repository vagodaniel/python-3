class toplista():
    def __init__(self,s):
        sor=s.split(";")
        self.sorszam=int(sor[0])
        self.helyezes=int(sor[1])
        self.cim=sor[2]
        self.eloado=sor[3]
        self.szarmazas=int(sor[4])
lista=[]
with open("toplista.txt", "r", encoding="utf-8") as f:
    for i in f:
        lista.append(toplista(i.strip()))
#2
print(len(lista)*3)
#3
for i in lista:
    if i.helyezes==1:
        print(f"{i.sorszam},{i.eloado},{i.cim}, ")
#4
db=0
szarmazas=[i.szarmazas]
for i in lista:
    if i.helyezes<=20:
        if i.szarmazas==1:
            db+=1
print(db)
#5
a=input("kerek egy eloadot:  ")
eloado=[]
for i in lista:
    if a in lista:
        print(f"{i.helyezes}")
    
