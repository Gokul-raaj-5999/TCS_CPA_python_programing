class Employee:
    def __init__(self,id,name,leaves):
        self.id=id
        self.name=name
        self.leaves=leaves

class Company:
    def __init__(self,cname,emps):
        self.cname=cname
        self.emps=emps

    def display_leaves(self,empid,Itype):
        for i in self.emps:
            if i.id==empid:
                for a,b in i.leaves.items():
                    if Itype==a:
                        return b

    def leave_application(self,empid,Itype,nol):
        for i in self.emps:
            if i.id==empid:
                for a,b in i.leaves.items():
                    if Itype==a:
                        if b>=nol:
                            return "Granted"
                        else:
                            return "Rejected"
if __name__ == '__main__':
    o=Company("PRO",emps=[])
    n=int(input())
    for i in range(n):
        leaves={}
    	id=int(input())
    	name=input()
    	leaves['EL']=int(input())
    	leaves['SL']=int(input())
    	leaves['CL']=int(input())
    	o.emps.append(Employee(id,name,leaves))
    empid=int(input())
    Itype=input()
    nol=int(input())
    print(o.display_leaves(empid,Itype))
    print(o.leave_application(empid,Itype,nol))
