class helsinki():
    def __init__(self,s):
        sor=s.split(" ")
        self.helyezes=int(sor[0])
        self.csapat=int(sor[1])
        self.sprotag=sor[2]
        self.verseny=sor[3]
lista=[]
with open("helsinki.txt" , "r" , encoding="UTF-8") as f:
    for i in f:
        lista.append(helsinki(i.strip()))
f.close()

#3
db=0
for i in lista:
    if i.helyezes<=6:
        db+=1
print(db)

#4
arany=0
ezust=0
bronz=0
for i in lista:
    if i.helyezes==1:
        arany+=1
    elif i.helyezes==2:
        ezust+=1
    elif i.helyezes==3:
        bronz+=1
    
print(f"arany:{arany}")
print(f"ezust:{ezust}")
print(f"bronz:{bronz}")
print(f"osszes:{arany+ezust+bronz}")

#5
hely=0
for i in lista:
    if i.helyezes==1:
        hely+=7
    if i.helyezes==2:
        hely+=5
    if i.helyezes==3:
        hely+=4
    if i.helyezes==4:
        hely+=3
    if i.helyezes==5:
        hely+=2
    if i.helyezes==6:
        hely+=1
print(f"osszesen: {hely}pont")

#6

#7
"""
ki=open("helsinki2.txt", "w" , encoding="utf-8")
   """
#8

 

    