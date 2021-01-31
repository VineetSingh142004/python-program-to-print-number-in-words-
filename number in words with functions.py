d1={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
d2={2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
d3={10:"ten",11:"eleven",12:"twelve",13:"therteen",14:"fourteen",15:"fifteen",16:"sixrteen",17:"seventeen",18:"eighteen",19:"nineteen"}
num=int(input("Enter Number :-"))
num_len=len(str(num))
def one(num):
    print(d1[num])
def two(num):
    if num<=19 and num>=10 :
        print(d3[num])
    elif num<=19 and num>=10 :
        print(d1[num])
    else :
        x=num//10
        if x==0:
            pass
        else :
            print(d2[x],end=" ")
        y=num%10
        if y==0:
            pass
        else :
            one(y)
def three(num):
    a=num//100
    if a==0:
        pass
    else :
        print(d1[a],"hundred",end=" ")    
    y=num%100
    if y==0 :
        pass
    else :
        two(y)
def four(num) :        
    a=num//1000
    print(d1[a],"thousand",end=" ")
    y=num%1000
    if y==0:
        pass
    else :
        three(y)
if num_len==4 :
    four(num)
elif num_len==3 :
    three(num)
elif num_len==2 :
    two(num)
else :
   one(num)