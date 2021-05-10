class item():
    def __init__(self,iname,itq,iup):
        self.iname = iname
        self.itq = itq
        self.iup = iup

class store():
    def __init__(self,dic):
        self.dic = dic

    def add(self,iname,itq,iup):
        i = item(iname,itq,iup)
        self.dic[iname]=[itq,iup]


    def callbill(self,rname,rq):
        #print("ih"self.dic[rname][0],,self.dic[rname][1])
        for i in range(0,len(self.dic)):
            if rname in self.dic.keys():
                #print(self.dic.keys(ranme))
                if(self.dic[rname][0]==0):
                    return(None)
                elif(self.dic[rname][0]>=rq):
                    tem = self.dic[rname][1]*rq
                    self.dic[rname][0] = self.dic[rname][0]-rq
                    return(tem)
                elif(self.dic[rname][0]<rq):
                    tem = self.dic[rname][1]*self.dic[rname][0]
                    self.dic[rname][0] = 0
                    return(tem)
        else:
            return(None)

    def pri(self):
        for i in self.dic.keys():
            print(i,(self.dic.get(i))[0])


n = int(input())
dic = {}
s = store(dic)
for i in range (0,n):
    iname = input()
    iup = int(input())
    itq = int(input())
    s.add(iname,itq,iup)
#s.pri()

r = int(input())
for i in range(0,r):
    rname = input()
    rq = int(input())
    print("Bill of item",rname,"=",s.callbill(rname,rq))
s.pri()
