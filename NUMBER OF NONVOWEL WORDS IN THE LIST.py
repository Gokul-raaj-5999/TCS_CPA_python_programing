def NonvowelWords(str_list):
    res=[]
    for i in str_list:
        z=0
        for j in i:
            if(j=='a'or j=='e' or j=='i' or j=='o' or j=='u'):
                z+=1
        if(z==0):
            res.append(i)
        else:
            z=0
    return res

if __name__ == '__main__':
    count=int(input())
    str_list=[]
    for i in range(count):
        str_list.append(input())
    result=NonvowelWords(str_list)
    if(len(result)>0):
        for i in result:
            print(i)
    else:
        print("no words are there with out vowels")
