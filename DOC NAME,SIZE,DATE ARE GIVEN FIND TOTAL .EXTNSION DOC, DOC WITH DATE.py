'''
input bellow...
4
101
gokul.ppt
10/10/2020, gokul, 5MB
102
ashwin.docx
ashwin, 24MB
103
guru.ppt
02/03/2001, guru, 21MB
104
partha.ppt
01/01/2001, partha, 1MB
docx
'''
class document():
    def __init__(self,did,dname,date,name,size):
        self.did = did
        self.dname = dname
        self.date = date
        self.name = name
        self.size = size

class docach():
    def __init__(self,dlist):
        self.dlist = dlist

    def add(self,did,dname,date,name,size):
        do = document(did,dname,date,name,size)
        self.dlist.append(do)

    def pri(self):
        for i in self.dlist:
            if (i.date):
                print(i.did,end=" ")
                print(i.date)

    def count(self,font):
        c = 0
        for i in self.dlist:
            if font in i.dname:
                c+=1
        print(c)

n = int(input())
dlist = []
d = docach(dlist)
for i in range (0,n):
    date = ""
    name = ""
    size = ""
    did = int(input())
    dname = input()
    ddet = input().split(",")
    #print(ddet)
    for j in ddet:
        if "/" in j:
            date = j
        elif "MB" in j:
            size = j
        else:
            name = j
    #print(date, name, size)
    d.add(did,dname,date,name,size)
font = input()
d.pri()
d.count(font)
