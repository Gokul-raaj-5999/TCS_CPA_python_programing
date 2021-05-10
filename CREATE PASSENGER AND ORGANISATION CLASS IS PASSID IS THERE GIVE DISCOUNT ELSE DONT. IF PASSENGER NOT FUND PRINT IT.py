class Passenger:
    def __init__(self,id,name,gender,miles):
        self.pass_id=id
        self.pass_name=name
        self.pass_gender=gender
        self.pass_miles=miles
    def calculate_discount(self,discount_rate):
        discount=self.pass_miles*discount_rate/100
        return discount

class Organisation:
    def __init__(self,name,p_list):
        self.o_name=name
        self.pass_list=p_list

    def Calculate_discount(self,id,discount_rate):
        dis=0
        for i in self.pass_list:
            if(i.pass_id==id):
                dis=i.calculate_discount(discount_rate)
                if(discount_rate>0):
                    return dis
                else:
                    return -1
        return 0

if __name__ == '__main__':
    count=int(input())
    pass_list=[]
    for i in range(count):
        id=input()
        name=input()
        gender=input()
        no_of_miles=int(input())
        pass_list.append(Passenger(id,name,gender,no_of_miles))

    o=Organisation("TCS",pass_list)
    id=input()
    dis_rate=int(input())
    res=o.Calculate_discount(id,dis_rate)
    if(res!=0):
        if(res>0):
            print("the discount rate for",id,"is",res)
        else:
            print("the discount rate will not there for",id)
    else:
        print("no passenger is there for u r entry")
