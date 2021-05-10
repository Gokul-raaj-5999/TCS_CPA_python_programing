class Research:
    def __init__(self,research_id,research_topic,research_author,research_cost,research_department):
        self.research_id=research_id
        self.research_topic=research_topic
        self.research_author=research_author
        self.research_cost=research_cost
        self.research_department=research_department
class University:
    def __init__(self,univ_name,res_list):
        self.univ_name=univ_name
        self.res_list=res_list
    def get_maxResearchDepart(self):
        l=[]
        d={}
        c=0
        for i in self.res_list:
            a=i.research_department
            l.append(a)
        for j in l:
            d.update({j:l.count(j)})
        for v in d.values():
            if v>c:
                c=v
        for k,v in d.items():
            if v==c:
                return(k)
    def get_researchByTopic(self,t):
        l=[]
        for i in self.res_list:
            if i.research_topic==t:
                l.append(i)
        if len(l)==0:
            return(None)
        else:
            return(l)
n=int(input())
l1=[]
for i in range(n):
    id=int(input())
    topic=input()
    author=input()
    cost=int(input())
    depart=input()
    a=Research(id,topic,author,cost,depart)
    l1.append(a)

rt=input()
uname="RGPV"
b=University(uname,l1)
k=b.get_maxResearchDepart()
m=b.get_researchByTopic(rt)
print(k)
if m==None:
    print("No researches on the given topic")
else:
    for i in m:
        print(i.research_id,i.research_cost,i.research_department)
