class Paper:
    def __init__(self,no,year,name,price):
        self.no=no
        self.year=year
        self.name=name
        self.price=price

class Agency:
    def __init__(self,ndb):
        self.ndb=ndb

    def search( self,year):
        lst=[]
        for no,paper in self.ndb.items():
            if(paper.year==year):
                lst.append(paper)

        return lst

    def calc(self,name):
        sum=0
        for no,paper in self.ndb.items():
            if(paper.name==name):
                sum+=paper.price

        return sum

if __name__=='__main__':
    c=int(input())
    ndb={}
    for i in range(c):
        no=input()
        paper=Paper(no,int(input()),input(),int(input()))
        ndb[no]=paper

    year=int(input())
    name=input()

    agency=Agency(ndb)
    lst=agency.search(year)
    if(len(lst)==0):
        print("not found")
    else:
        for paper in lst:
            print(paper.no)
            print(paper.name)
            print(paper.year)
            print(paper.price)

    total=agency.calc(name)
    if(total==0):
        print("not found")
    else: print("Total Price: ",total)
