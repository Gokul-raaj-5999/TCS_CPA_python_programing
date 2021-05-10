class passenger():
    def __init__(self,pname,age,distance):
        self.pname=pname
        self.age=age
        self.distance=distance

def Cal_tick_price(plist,rate_pkm):
    t_price=0
    tax=0
    for i in plist:
        price=0
        price+=i.distance*rate_pkm
        if(i.age>=60 or i.age<12):
            tax=0
        elif(59>i.age>21):
            tax=0.12*price
        elif(12>=i.age>=20):
            tax=0.1*price
        price+=tax
        t_price+=price
    print(t_price)

def Countseniorjunior(plist):
    count=0
    for i in plist:
        if(i.age<12 or i.age>=60):
            count+=1
    print(count)

count=int(input())
plist=[]
for i in range(count):
    pname=input()
    age=int(input())
    dist=int(input())
    plist.append(passenger(nam,age,dist))
rate_per=int(input())
Cal_tick_price(plist,rate_per)
Countseniorjunior(plist)
