#print n natural number using recursion


##n=5
##def number(n):
##    if n==0:
##        return 0
##    
##    c=1+number(n-1)
##    print(c)
##    return c
##
##number(n)



#Sir's aproach ---------------
##n=5
##def n_nat(n):
##    if n<1:
##        return
##    n_nat(n-1)
##    print(n)
##
##n_nat(5)



# nth even natural number

##n=5
##
##def number(n):
##    if n==0:
##        return
##    
##    if n%2==0:
##        number(n-1)
##        print(n)
##    else:
##        number(n-1)
##    
##
##number(n)
    


## ' 1 2 3 2 1'
##temp=4
##def number(n=1):
##    if n==temp:
##        print(n,end=' ')
##        return
##        
##    print(n,end=' ')
##    number(n+1)
##    print(n,end=' ')
##    
##number()



##n=3
##res=""
##i=1
##def pat(n):
##    global res
##    if n<1:
##        return
##
##    for i in range(1,n):
##        pat(i)
##        
##        pat(n-i)
##
##    res+="("
##    pat(n-1)
##    res+=")"
##
##
##pat(n) 
##print(res)


##def sum_n(n,i=0,res=0):
##    if i>10:
##        return res
##    res+=i
##    return sum_n(n,i+1,res)
##
##print(sum_n(10))

## WAP to flaten any given list


ls=[4,[4,6],[[1,5],2]]

##res=[]
def flatten(ls):
    res=[]
    for i in ls:
        if type(i)==list:
            res+=flatten(i)
            
        else:
            res.append(i)
            
    return res
            
    

    
print(flatten(ls))

























    
