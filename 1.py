 #1
"""
a=int(input("kerek egy szamot:"))
if a==2:
    print("Prím") 

elif a%a==0 and a%1==0 and a%2==1:
    print("prím")

else:
    print("nem prim")

 """
#2
"""
k=int(input("kerek egy szamot"))
print(f"y={1*2+2*3+3*4+k*(k+1)}")
"""
#3
"""
import random
random.randint
"""
#4
"""
n=int(input("egyik szam"))
m=int(input("masik szam"))

"""
#5
"""
a=str(input("Vidd ki a szemetet!"))
while  

"""



"""
#Írj egy programot, amely kiírja a páros számokat 1 és 10 között!

szam = 1
while szam <= 10:
    if szam%2==0:
        print(szam)
    szam = szam + 1     
"""
"""
#Írj egy programot, amely csökkenő sorrendben írja ki a számokat 1 és 10 között!  

szam = 10
while 1<=szam <= 10:
    print(szam)
    szam = szam - 1 
"""
"""
#Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!
szam = 10
while 1<=szam <= 10:
    if szam%2==1:
        print(szam)
    szam = szam - 1 
"""
#Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!
"""
a=input("szoveg")
b=int(input("hanyszor irjam le"))
i=1
while i<=b:
    print(a)
    i=i+1
"""



#Írj egy programot, amely a felhasználótól páros számot kér be.
# Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, 
# amíg végül páros számot nem ad meg a felhasználó.

"""
szam = int(input('Adj meg egy páros számot  '))

  # while szam < 5 or 10 < szam:
while not szam%2==0:
      szam = int(input('Helytelen érték! Adj meg egy páros számot! '))
  
print('Rendben!')     
  
"""

#Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot!
#  A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, 
# hány darab ilyen szám volt.
"""
import random

veletlenszam=[1,2,3,4,5,6,7,8,9,10,11,12]
print("list before shuffle:", veletlenszam)
random.shuffle(veletlenszam)
print("list after",veletlenszam)
"""

import random
a=random.randint(1,12)
i=0
db=0
while i<=20:
    if a%3==0:
        db+=1
        print(a)
    a=random.randint(1,12)
    i+=1
print (f"{db} 3mal oszthato szam volt")



