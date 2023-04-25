n=int(input("mennyi etelt szallitott ki:  "))
m=int(input("mennyi mosolygos fejet kaptal:  "))
szazalek=(n/m)*100
bonuszpenz=[]
if szazalek>=25:
    bonuszpenz.append(50000)
elif 50<szazalek<=75:
    bonuszpenz.append(100000)
elif 75<szazalek<=90:
    bonuszpenz.append(150000)
else:
    bonuszpenz.append(200000)
print(f"a futar {n}db etelt szallitott ki, {m}db mosolygos fejet kapott, {szazalek}% ban kapott mosoéygos felyet, bonusza:{bonuszpenz}")