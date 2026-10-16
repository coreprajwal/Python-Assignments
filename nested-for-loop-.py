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



n=5
for i in range(n+1):
    print(f'{"* "*i:^10}')
   

















