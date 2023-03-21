class vedett():
    def __init__(self,s):
        sor=s.split(";")
        self.nev=sor[0] 
        self.darab=int(sor[1]) 
        self.ev=int(sor[2]) 
        self.faj=sor[3]
lista=[]
with open("vedett.txt","r", encoding="UTF-8") as fuck:
    for i in fuck:
        
        