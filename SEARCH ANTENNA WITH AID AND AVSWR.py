""" sample input
111
reconfigurable
hema
0.4
222
weariable
kavya
0.9
333
microstrip
teju
0.3
444
dielectric
sai
0.65
microstrip
0.5 
"""

class antenna():
    def __init__(self,aid,aname,plead,avswr):
        self.aid = aid
        self.aname = aname
        self.plead = plead
        self.avswr = avswr

class myclass():
    def __init__(self,alist):
        self.alist = alist
        
    def searchantenna(self,fant):
        for i in self.alist:
            if(i.aname==fant):
                print(i.aid)
                print(i.plead)
                return 0
        else:
            print("There is no Antenna with the given parameter")
        
        
    def sortantenna(self,favswr):
        try:
            x=[]
            for i in self.alist:
                if(i.avswr<=favswr):
                    x.append(i.avswr)
            x.sort(reverse = True)
            #print(x[0])
            for i in self.alist:
                if(x[0]==i.avswr):
                    print(i.plead)
        except:
            print("No antenna found")
        
        
        

n = 4
alist=[]
mc = myclass(alist)
for i in range(0,n):
    aid = int(input())
    aname = input()
    plead = input()
    avswr = float(input())
    a = antenna(aid,aname,plead,avswr)
    alist.append(a)
    
fant = input()
favswr = float(input())
mc.searchantenna(fant)
mc.sortantenna(favswr)
    
    
    
    
    
    