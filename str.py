"""
s="1a1l1m1a1"
print(s[0]) #elso betu 'a'
print(len(s)) #string hossza:
print(s[len(s)-1]) #utolso karakter
#szeletelés:
print(s[1:])
print(s[1:3]) #lecsip egyet ejnye py
print(s[::-1])
print(s[2::-1])
#stringek osszefuzese
s1="fa"
print(s+s1)

nev=str(input("egy nev:"))
print(nev[0]+nev[nev.index(" ")+1])


#direkt törlés nincs!!!

s[0]='A' 
print(s)


s='A'+s[1:] #kicsereli az elso betut
print(s)

#osszehasonlitas 
if s==s1:
    print("egyforma he")
elif s>s1:
    print("s1 szoveg hamarabb van")
else:
    print("s1 van hatrebb")
import locale
print(locale.strcoll(s,s1))
#eldont
tar="a" in s
print("van" if tar else "nicscs")

#string kezelo fuggvenyek
print(s.count("l"))# hany l van bene
print(len(s))# hosz
print(s.index('l'))# l betu hanyadik indekszu
print(s.find('k'))
#az index nem letezo esetkent kidob, a 'find' pedig -1 el jon vissza ha nem letezik
s=s.replace('a', 'e').replace('l','f')#csere
print(s)
#kis/nagybetus atalakitas
s=s.upper()#/lower
print(s)
print(s.lower())
print(s.swapcase())#kis nagy betu csere
print(s.capitalize())#kiskapitalis

#van e bene szam
print(s.isalpha())
print(s.isdigit())

#hany szam van bene
db=0
for i in s:
    if i.isdigit():
        db+=1
    
print(db)
print(len(s)-db)

kod=ord(s[0])
print(kod)
print(f'{s[0]}')
print(f"{kod}-{s[0]}")
print(chr(kod))

#s string betu kod
for i in s:
    print(f"{ord(i)}-{i}")

#elso es utolso betu vizsgalata
print(s.startswith('a'))
print(s.endswith('a'))
#adott stringet listaelemekre bont
m=input("egy mindat:     ")
lista=[]
#torles
m=m.replace(".","")
print(m)
lista=m.split()
print(lista)
uj=("mi").join(lista)
print(uj)
#szokoz eltavolitasa:
p=" körte"
print(len(p))
p=p.strip()
print(len(p))
"""

#olvass be egy szot es ird ki a betuit ugy hogy kozottük szkokoz legyen

k=input("ker k 1 db syot:   ")
for i in k:
   print(i+" ", end=" ")
"""

"""

tabu=input("betu ami ne legyen benne:   ")
k=k.replace(tabu,"")
print(k)


i=0
while i<len(k):
    print(k[i], end="")
    i+=2

print(k[::-1])

mondat=input("kerek egy mondat:   ")

l=[]
l=mondat.split()

for i in l:
    print(i)