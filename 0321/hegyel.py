class hegyek:
    def __init__(self,s):
        sor=s.split(";")
        self.hegycsucs=sor[0] 
        self.hegy=sor[1] 
        self.magassag=int(sor[2]) 
fejlec=""
lista=[]
with open("hegyekMo.txt","r",encoding="UTF-8") as f:
    fejlec=f.readline()
    for i in f:
        lista.append(hegyek(i.strip()))
f.close()
print(f"hegycsucsok szama{len(lista)}")
lista1=[]
for i in lista:
    lista1.append(i.magassag)
legmagasabb=max(lista1)
for i in lista:
    if legmagasabb==i.magassag:
        print(i.hegycsucs)

magassagertek=int(input("magassag:   "))
van=False
for i in lista:
    if i.hegy=="Börzsöny":
        if i.magassag>magassagertek:
            van=True
if van==True:
    print("van benne")
else:
    print("nincs benne")
"""
db=()
for i in lista:
    i.magassag*3.280839895>3000
    db+=1
print(db)
szotar=()
for i in lista:
    if i.hegy in szotar:
        szotar[i.hegy]+=1
    else:
        szotar[i.hegy]=1
for 
"""
ki=open("bukk.txt","w", encoding="utf-8")
ki.write(fejlec)
for i in lista:
    if i.hegy=="Bükk-vidék":
        ki.write(i.hegycsucs+":"+str(round(i.magassag*3.280839895)))
ki.close()