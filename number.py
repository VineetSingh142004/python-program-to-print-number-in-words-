d1={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
d2={2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
d3={10:"ten",11:"eleven",12:"twelve",13:"therteen",14:"fourteen",15:"fifteen",16:"sixrteen",17:"seventeen",18:"eighteen",19:"nineteen"}
num=int(input("Enter Number :-"))
num_len=len(str(num))
if num_len==3 :
    x=num//100
    print(d1[x],end=" ")                            
    print("hundred",end=" ")
    y=num%100
    if y<=19 and y>=10 :
        print(d3[y])
    elif y<10 and y>0 :
        print(d1[y])
    else :
        x=y//10
        if x==0 :
            pass
        else :
            print(d2[x],end=" ")
        z=y%10
        if z==0 :
            pass
        else :
            print(d1[z])
elif num_len==2 :
    if num<=19 :
        print(d3[num])
    else :
        x=num//10
        print(d2[x],end=" ")
        y=num%10
        if y==0 :
            pass
        else :
            print(d1[y])
else :
    print(d1[num])

