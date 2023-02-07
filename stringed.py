"""
def csillag(s):
    print(len(s)*"*")
csillag("ablak")
"""

def szamok(szam):
    if szam<=0:
        print("HIBA!")
    else:
        uj=""
        for i in range(szam):
            if i%3==0:
                uj+="+"
            else:
                uj+="-"
    print(uj)
szamok(20)

def mondat(s):
    print(s[::-1])
mondat("sut a nap")

def szokoz8(s):
    s=s.replace(" ","")
    print(s)
szokoz8("igen nem igen nem")

lista=['Én', 'elmentem', 'a', 'vásárba', 'fél', 'pénzen.']
print(len(lista))
van=False
for i in lista:
    if "." in i:
        van=True
print("van benne" if van else "nincs benne")

print(lista.count("a"))
print(lista.count("az"))

print(lista.index("fél"))

#Van-e a mondatban nagy kezdőbetűs szó, és ha igen, akkor hol?

nincs=False
for i in lista:
    if i[0].isupper():
        nincs=True
print("van benne" if nincs else "nincs benne")

def masol(s1, s2):
    index=len(s2)
    uj=s2+s1[index:]#fa+ma
    return uj
print(masol("alszol","fa"))

def karakter(kar, s):
    index=s.find(kar)
    if index==+1:
        return "niccs benne ilyen karakter"
    else:
        return index
print(karakter("a", "alma"))

def betuk(s):
    uj=""
    for i in s:
        if i.isupper():
            uj+=i.lower()
        else:
            uj+=i.upper
    return uj
print(betuk("En egy erdoben allok"))

def fesul(s1,s2):
    uj=""
    for index in range(len(s1)):
        uj+=s1[index]+s2[index]
    return uj
print(fesul("alma", "123"))

