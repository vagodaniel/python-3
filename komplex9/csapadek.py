import random
lista=[]
for i in range(10):
    x=random.randint(0,30)
    lista.append(x)
    print(x)
print(sum(lista))
print(sum(lista)/len(lista))

def paros(szam):
    if szam%2==0:
        return True
    else:
        return False
for i in lista:
    if paros(i)==True:
        print(i, end=" ")
print("\n-------")
for i in lista:
        if paros(i)==False:
            print(i, end=" ")
    
