def palindrome_list(l):
       res=[]
       for i in l:
             j=i.lower()
             if(j==j[::-1]):
                    res.append(i)
       return res

if __name__ == '__main__':
       count=int(input())
       input_list=[]
       for i in range(count):
             input_list.append(input())
       result=palindrome_list(input_list)
       for i in result:
             print(i)
