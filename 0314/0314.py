f=open("kutya.txt", "r", encoding="utf-8")
lista=[]
for i in f:
    lista.append(i.strip())
print(lista)
#hany adat van
print(len(lista))
#max
maxhossz=len(lista[0])
maxi=0
for i in range(len(lista)):
    if len(lista[i]) > maxhossz:
        maxhossz=len(lista[i])
        maxi=i
print(lista[maxi])
#Hány olyan név van, amely 5 karakter hosszú függvénnyel?
db=0
for i in lista:
    if len(i)==5:
        print(i)
        db+=1
print(db)