a=int(input("hany liter: "))
b=int(input("milyen hosszu utat tesz meg:  "))
print(f"az uzemanyag tartaly urtartalma: {a}")
print(f"teljes tankkal megtett ut hossza: {b}")
fogyasztas=a/b*100
if fogyasztas<6.5:
    print(f"Az on autojanal fogyasztasa alacsony: {fogyasztas:.1f}/100km")
elif 6.5<fogyasztas<8.5:
    print(f"Az on autojanal fogyasztasa atlagos: {fogyasztas:.1f}/100km")
else:
    print(f"Az on autojanal fogyasztasa magas: {fogyasztas:.1f}/100km")
