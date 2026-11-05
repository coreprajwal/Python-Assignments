##def add(a,b):
##    '''This method will add 2 values and return the result'''
##    c=a+b
##    return c
##    print("Hello")
##
##
##print(add(2,2))
##
##print(add.__doc__)



##def add(a,b):
##    '''This method will add 2 values and return the result'''
##    c=a+b
##    print(c)
##    print("Hello")
##
##
##print(add(2,2))
##
##print(add.__doc__)


## Wa function to check whether the given number is a odd number
## or even number

##def isodd_even(a):
##    if a%2:
##        return "odd"
##    else:
##        return "even"
##
##
##print(isodd_even(3))
##print(isodd_even(4))


## Wap to check whether the given number is even or not

##def iseven(a):
##    return a%2==0
##        
##n=int(input("Enter number:"))
##print(iseven(n))


## Wap to calculate the factorial of the number

##
##def factorial_(n):
##    s=1
##    while n>0:
##        s*=n
##        n-=1
##    return s
##
##print(factorial_(4))


## WAF to check whether the number is a strong number or not
## Factorial of digits and addition should be equal to original number
    
##def factorial_(n):
##    s=1
##    while n:
##        s*=n
##        n-=1
##    return s
##
##def isstrong(n):
##    res=0
##    for i in str(n):
##        res+=factorial_(int(i))
##    return res
##          
##    
##n=int(input("Enter number:"))
##
##if isstrong(n)==n:
##    print("Its a strong number:")
##else:
##    print("Its not a strong number.")



## Print this pattern 12321 for n as 3


##def pattern(n):
##    res=0
##    for i in range(1,n):
##        res =res*10+i
##    for i in range(n,0,-1):
##        res =res*10+i
##    return res
##
##n=int(input("Enter number:"))
##print(pattern(n))


## Flatten this list
##a=[[1,[1,3,10,2],4],6,7,[5,[8,9]]]
##ls=[]
##
##def nest_list(a):
##    for i in a:
##        if type(i)==type([]):
##            for j in i:
##                if type(j)==type([]):
##                    ls.extend(j)
##
##                else:
##                    ls.append(j)
##        else:
##            ls.append(i)
##nest_list(a)
##print(ls)
        


# Wap to flatten any given nested list

##a=[[1,[1,3,10,2],4],6,7,[5,[8,9]]]
##
##a=str(a).replace("]","").replace("[","").replace(" ","")
##print(list(eval(a)))


##ls=[]
##for i in a:
##    ls.append(int(i))
##print(ls)

##str(a).replace("]","")


    
##ls=[]
##def nest_list(n):
##    temp=[]
##    for i in a:
##        if type(i)==type([]):
##            temp.extend(j)
##            temp=nest_list(j)
##            ls.extend(temp)
##            return temp
##            else:
##                ls.append(j)
##        else:
##            ls.append(i)
##
##nest_list(a)
##print(ls)



##Wap to check whether the given number is an armstrong number or not


##n=153
##res=0
##
##def isarmstrong(n):
##    digits=len(str(n))
##    temp=n
##    res=0
##    while temp:
##        rem=temp%10
##        res+=rem**digits
##        temp=temp//10
##        
##    return res==n
##    
##
##print(isarmstrong(152))



##for i in str(n):
##    res+=int(i)**(len(list(str(n))))
##
##if n==res:
##    print("Its an armstrong number:",res)
##else:
##    print("Its not an armstrong number")






## ARGUMENTS ---------------------------------


##def demo(a,b,c,d,e):
##    print(a,b,c,d,e)
##
##demo(10,20,30,40,50)
##demo(10,20,c=30,e=50,d=40)

##demo(10,20,30,c=100,d=40,e=50) ## Error

##demo(10,20,30,d=40,500)


# Positional only arguments ------------

##def add(a,b,c):
##    print(a,b,c)
##
##add(10,20,30)
##add(a=10,b=20,c=30)

##def add(a,b,c,/): ## / represent positional only arguments.
##    print(a,b,c)
##
##add(10,20,30)
##add(a=10,b=20,c=30)


# Keyword only argument ------------
##def info(*,name ,age, ph_no, add): ## '*' represents keyword only arguments
##    print(name,age,ph_no,add)
##
##info(name="anurag",age=20,ph_no=2353253252,add="purvanchal")


# Combination on position only and keyword only

def info(name,/,age,*,dob,add):
    print(name,age,dob,add)

##info ("anurag",20,'8-3-2006','mumbai')# error- 4 positional args

info("anurag",20,dob='8-11-2006',add='mumbai')











