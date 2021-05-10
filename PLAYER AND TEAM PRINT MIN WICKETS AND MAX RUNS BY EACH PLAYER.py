class player():
    def __init__(self,pname,pctry,page,nom,nor,now):
        self.pname = pname
        self.pctry = pctry
        self.page = page
        self.nom = nom
        self.nor = nor
        self.now = now

class team():
    def __init__(self,plist):
        self.plist = plist
    def addplayer(self,pname,pctry,page,nom,nor,now):
        p = player(pname,pctry,page,nom,nor,now)
        self.plist.append(p)
    def gmr(self):
        for i in self.plist:
            tnam = i.pname
            tctry = i.pctry
            trun = i.nor
            #max runs
            for j in plist:
                if trun>j.nor:
                    tnam = j.pname
                    tctry = j.pctry
                    trun = j.nor
        print(tnam)
        print(trun)
        print(tctry)
    def gmw(self):
        for i in self.plist:
            tnam = i.pname
            tctry = i.pctry
            twic = i.now
            #min wic
            for j in plist:
                if twic>j.now:
                    tnam = j.pname
                    tctry = j.pctry
                    twic = j.now
        print(tnam)
        print(twic)
        print(tctry)

n = int(input())
plist = []
t = team(plist)
for i in range(0,n):
    pname = input()
    pctry = input()
    page = int(input())
    nom = int(input())
    nor = int(input())
    now = int(input())
    t.addplayer(pname,pctry,page,nom,nor,now)
t.gmr()
t.gmw()
