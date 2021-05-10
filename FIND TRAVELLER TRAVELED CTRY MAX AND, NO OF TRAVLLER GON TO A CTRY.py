class traveler():
    def __init__(self,tname,clist,tage,tfrom):
        self.tname = tname
        self.clist = clist
        self.tage = tage
        self.tfrom = tfrom

class travelagent():
    def __init__(self,tlist):
        self.tlist = tlist
    def counttraveled(self,findctry):
        count = 0
        for i in tlist:
            for j in range(0,len(i.clist)):
                if i.clist[j]==findctry:
                    count+=1
        print(count)
    def maxctrytraveled(self):
        count = 0
        name = ''
        for i in tlist:
            if len(i.clist) > count:
                count = len(i.clist)
                name = i.tname
        print(name)


n = int(input())
tlist = []
ta = travelagent(tlist)
for i in range (0,n):
    clist = []
    tname = input()
    nl = int(input())
    for j in range(0,nl):
        clist.append(input())
    tage = int(input())
    tfrom = input()
    tlist.append(traveler(tname,clist,tage,tfrom))
findctry = input()
ta.counttraveled(findctry)
ta.maxctrytraveled()
