##for i in range(1,4):
##    for j in range(3):
##        print(i,j)


# WAP to print a square star pattern

##
##n=4
##for i in range(n):
##    print("*"*n)

# WAP to print a pyramid pattern with single loop and
##print statement

##n=30
##for i in range(n):
##    print(" "*(n-i)+"* "*i)


# Wap to check whether the given number is a palindrome or not
# and if it is a palindrome check whether the palindrome is a
# armstrong number or not and if it is armstrong check if it is
##even or odd without typecasting


##num=2
##n=num
##d=[]
##r=0
##c=0
##a=0
##while n!=0:
##    c+=1
##    rem=n%10
##    d.append(rem)
##    r=r*10+rem
##    n=n//10
##
##print(f"n:{num}, r:{r}")
##if num==r:
##    for i in d:
##        a+=i**c
##
##else:
##    print("Not a palindrome")
##
##if a==num:
##    if a%2:
##        print("Palindrome, Armstrong and odd number")
##    else:
##        print("Palindrome, Armstrong and even number")
##
##else:
##    print("Palindrome but not an armstrong number")




#WAP to check whether the given number is a strong number or not.
##n=145
##ls=[]
##temp=str(n)
##for i in temp:
##    f=1
##    for j in range(1,int(i)+1):
##        f*=j
##    ls.append(f)
##
##if sum(ls)==n:
##    print("it is a strong number:",sum(ls),"ls:",ls)
##else:
##    print("Not a strong number.","ls:",ls)



# WAP to find duplicate pairs that sums to give the number n



#matrix multiplication

# wap to find if a number is a flyod number or not

# WAP to print triangle star pattern

##n=4
##
##for i in range(1,n+1):
##    print(f"{i}th line:",end="")
##    for j in range(i):
##        print("*",end="")
##    print()

##n=5
##
##for i in range(1,n+1):
##    if i in [1,n]:
##        for j in range(n):
##            print("*",end="")
##        print()
##    else:
##        print("*"+(" "*(n-2))+"*")

##n=5
##
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i in (1,n) or j in (1,n):
##            print("*", end="")
##        else:
##            print(" ", end="")
##            
##    print()



# Print a,b,c,d in triangle with nested loop


##n=5
##a=ord("A")
##for i in range(1,n+1):
##    for j in range(i):
##        print(chr(a),end="")
##        a+=1
##    print()



##n=5
##for i in range(n+1):
##    print(f'{"* "*i:^10}')
   

# Sum of integer numbers

##ls=[1,-5,2,0.5]
##
##summ=0
##for i in ls:
##    if type(i)==type(5):
##        summ+=i
##
##print(summ)


##s="Hello"
##r=""
##
##for i in range(-1,(-len(s)+1,-1):
##    r+=s[i]
##
##print(r)


# WAP to find 10th prime number
##n=10
##count=0
##x=1
##
##while count<n:
##    x+=1
##    flag=True
##    for i in range(2,x):
##        if x%i==0:
##            flag=False
##    if flag:
##        count+=1
##print(x)
    
##num=10
##n=2
##count=0
##while count<=num:
##    flag=True
##    for i in range(2,count):
##        if n%i==0:
##            flag=False
##    if flag:
####        print("prime",n)
##        count+=1
##    n+=1
##
##print(n-1)


# Check if a number is perfect number or not
##n=28
##s=0
##i=1
##
##while i<n:
##    if n%i==0:
##        s+=i
##    i+=1
##if s==n:
##    print("Its a perfect number:",s)


# Print 6th perfect number
##n=6
##i=2
##count=0
##
##while count!=n:
##    s=0
##    c=1
##    while c<n:
##        if i%c==0:
##            s+=c
##        c+=1
##        
##    if s==c:
##        print("Its a perfect number:",c)
##        count+=1
##    
##    i+=1
##print()

# Wap to find nth palindrome number

##n=10
##i=1
##count=0
##
##while count!=n:
##    if str(i)==str(i)[::-1]:
##        count+=1
##    i+=1
##print(i-1)



##n=1000
##count=0
##x=1
##
##while count<n:
##    res=0
##    temp=x
##    while temp:
##        last=temp%10
##        res=res*10 + last
##        temp//=10
##    if res==x:
##        count+=1
##    x+=1
##print(x-1)


# Addition between 2 matrix

##m1=eval(input("Enter matrix 1:"))
##m2=eval(input("Enter matrix 2:"))
##
##r=[]
##
##for i in range(len(m1)):
##    t=[]
##    for j in range(len(m1[i])):
##        t.append(m1[i][j]+m2[i][j])
##    r.append(t)
##
##print(r)


##m1=eval(input("Enter matrix 1:"))
##m2=eval(input("Enter matrix 2:"))
##
##r=[]
##
##for i in range(len(m1)):
##    r.append([])
##    for j in range(len(m1[i])):
##        r[i].append(m1[i][j]+m2[i][j])
##
##print(r)
        
    
# Wap transpse



##m=[[1,6,3],[4,2,8],[2,1,9]]
##r=[]
##
##for i in range(len(m)):
##    r.append([])
##    for j in range(len(m[i])):
##        r[i].append(m[j][i])
##
##print(r)


# WAP to check if a number is strong or not

n=145
r=0
for i in str(n):
    s=1
    for j in range(1,int(i)+1):
        s*=j
    r+=s

if n==r:
    print("Strong number:",r)
else:
    print(r)
        
        








    




