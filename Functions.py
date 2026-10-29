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



## Print this patter 12321 for n as 3


def pattern(n):
    res=0
    for i in range(1,n):
        res =res*10+i
    for i in range(n,0,-1):
        res =res*10+i
    return res

n=int(input("Enter number:"))
print(pattern(n))











