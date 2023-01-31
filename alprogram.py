"""
Alprogram: olyan programrész, amelyet a programban többször is használhatjuk, de elég csak egy helyen módosítani. Két fajtája: az eljárás és a függvény.
Eljárás: Olyan alprogram, amely valamilyen tevékenységet hajt végre.
(Az alprogram egy programrészletet jelent)

Függvény: Olyan alprogram, amely valamilyen értéket állít elő.

A függvény és eljárásokat összességében metódusnak is szokták mondani.
Eljárásra példa:

def függvény_neve():
	utasítások
	
Paraméterek megadása a () között lehet.

Pl.
def koszon(nev):		nev formális paraméter, csak 		    print("Helló "+nev+"!")	eljáráson belül létezik
	
kiir("Márk")		Eljárás meghívása, ahol	"Márk" az aktuális paraméter
Függvényre példa:

Érték visszaadása: A függvény törzsén belül a return utasítással
def osszead(a,b):
	return a+b

print(osszead(5,7)) Függvény meghívása, ahol aktuális paraméterek: 5,7.

Ha egy változót, amit kívül adtunk meg, szeretnénk módosítani az eljárás vagy függvényen belül, akkor a belső részében ki kell adni a global kulcsszót.
Pl. xyz=5
def fuggveny():
	global xyz
	xyz=10		#Az xyz változó értéke ténylegesen 10 lesz
	
"""

"""
#szam osztoinak meghatarozasa eljarassal

def osztoi(szam):#100-1,2,5,10,20,25,50,100... stb
    oszto=1
    while oszto<szam:
        if szam%oszto==0:
            print:(oszto)
        oszto+=1
 #fuggveny meghivasa
osztoi(50)
osztoi(120)
"""
"""
#szam osztoi meghat. fuggvennyel
def osztok(szam):#100-1,2,5,10,20,25,50,100... stb
    oszto=1
    l=[]

    while oszto<szam:
        if szam%oszto==0:
            l.append(oszto)
        oszto+=1
    return l#visszaadott erteke
print(osztok(50))
"""
"""
def osszeg(a,b):
    return a+b
print(osszeg(4,5))
"""
"""
def paros(szamok):
    l=[]
    oszto=0
    if szamok%2==0:
        l.append(oszto)
        oszto+=1
print(paros(50))


"""

"""
def leghosszabb_szo(s): #ma nem veszek alma
    if s=="":
        return "HIBA!"
    else:

         l=s.split() #l= ma,nem,veszek,alma
         #maximum kivalasztas tetele
         max=len(l[0]) #2
         maxi=0
         for i in range(len(l[0])):
             if max<len(l[i]):
                 max=len(l[i])
                 maxi=i
         return l[maxi]
    print(leghosszabb_szo(input("kerek 1 mondatot:")))
"""
"""

# lista=["fgb","jelszo123", "asdfghjkl", "123nnoob", "1ufnuhuoHUBJbueu379246328752"]
def gyenge_jelszavak(lista):
    gyenge=[]
    for i in lista:
        if i<5:
            gyenge.append(i)
        elif i.isalpha():
            gyenge.append(i)
        elif "jelszo" in i or "123":
            gyenge.append(i)
    return (gyenge)
    lista=["fgb","jelszo123", "asd", "123nnoob", "1ufnuhuoHUBJbueu379246328752"]
    print(gyenge_jelszavak(lista))

"""
"""
def egyedi_szavak_szama(s): #máma nem eszunk kaposztat piyokaval
    s=s.lower()
    s=s.replace
"""

def felvaltva(s):
    l=s.split()
    if len(l)<2:
        return "hiba"
    else:
        for i in range(len(l)):
            if i%2==0:
                l[i]=l[i].upper()
            else:
                 l[i]=l[i].lower()
    uj=(" ").join(l) 
    return l
print(felvaltva("lorem lore m lorem morel morle lorem lorem lorem orem oerm emkng "))
