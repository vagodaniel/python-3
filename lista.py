import turtle

"""
honapok=["januar" , "februar" , "marcius" , "aprilis" , "majus" , "junius" , "julius" , "augusztus" , "szeptember" , "oktober" , "november" , "december"]
print(honapok)
print(',' .join(honapok))
print(len(honapok))
print(honapok[0])
print(honapok[len(honapok)-1])
print(honapok[1:5])
print(honapok[1:])
print(honapok[:4])
print(honapok[::-1])
print(honapok[::-2])
print(honapok[-2:6:-1])
"""

honapok=["januar" , "februar" , "marcius" , "aprilis" , "majus" , "junius" , "julius" , "augusztus" , "szeptember" , "oktober" , "november" , "december"]
for ho in honapok:
    print(ho)

for index in range(len(honapok)):
    print(index, honapok[index])

for index, honap in enumerate(honapok, start=10):
    print(index,honapok)

ho_masolat=honapok
ho_masolat.sort()
print(ho_masolat)
print(sorted(honapok))
print(honapok) 

print(honapok.index('januar'))
print(honapok.count('majus'))
print('majus' in honapok)

honapok.append('februar')
honapok_masolat=honapok.copy

uj_honapok=["augusztus" , "szeptember"]
honapok.extend(uj_honapok)


honapok.pop()
print(honapok)
honapok.pop(2)
print(honapok)
del honapok[3]
honapok.remove("februar")
print(honapok)

import random

szam=random.randint(1,99)
szamok=[] #ures lista ez
for i in range(5):
    szamok.append(random.randint(1,99))
print(szamok)
print(sum(szamok))

szamok1=[] #ures lista ez
for i in range(5):
    szamok1.append(random.randint(1,99))
uj_szamok=szamok+szamok1
print(uj_szamok)
print(szamok*3)

eredmeny=[x*2 for x in szamok]
print(eredmeny)
eredmeny1=[x**2 for in szamok if x%2==0]