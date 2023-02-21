import random
"""
telnev=input("telepules: ")
iszam=input("iranyito: ")

def kod(s,szam):
    return s[0:2]+str.szam+str(random.randint(10,99))

print(kod(telnev, iszam))
"""
"""
mondat=input("mondat: ")

def valtozo(s):
    s=s.lower()
    betu=s[0]
    karakter=s.count(betu)
    return karakter/len(s)
print(f"{valtozo(mondat)*100:.1f}%")
"""
"""
lista=[]
def feltolt():
    for i in range(1,366):
        if 1<=i<=59 or 335<=i<=365:
            lista.append(random.randint(40,70))
        elif 60<=i<=151:
            lista.append(random.randint(180,200))
        elif 152<=i<=243:
            lista.append(random.randint(350,400))
        else:
            lista.append(random.randint(80,120))
        
feltolt()
print(lista)
print(sum(lista)*1500)
print((sum(lista)*1500)-365*25000-50000000)
print(lista.index(max(lista)))
print(lista.index(min(lista)))
"""
"""
szoveg=input("mondat:   ")

def tavirat(s):
    s=s.upper()
    s=s.replace(","," ").replace("!",".").replace("?",".")
    lista=s.split(".")
    uj_szoveg=(" STOP").join(lista)
    return uj_szoveg
print(tavirat(szoveg))
"""
