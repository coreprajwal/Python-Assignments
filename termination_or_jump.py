##n=11
##
##for i in range(2,n):
##    if n%i==0:
##        print("Not a prime number")
##        break
##else:
##    print("Prime number")


# WAP to find all the divisors of a number but the iteration
# should stop after half of the number range

##n=int(input("Enter number:"))
##divisors=[]
##for i in range(1,n):
##    if i==(n//2)+1:
##        break
##        
##    if n%i==0:
##        divisors.append(i)
##print(divisors)
    
# WAP to take continuos input from the user until the input
# matches with the given string

##pw="prajwal123"
##
##while True:
##    i=input("Enter password:")
##    if pw==i:
##        break
##print("Succesfully Entered")



##Wap to take password verify whether the password is correct or not ,
##if password is not correct , then give hint to the user,
##with every newly entered password give a new hint

##pas="prajwal123"
##duplicates={}
##
##for i in range(len(pas)-1):
##    if (pas[i] in pas[i+1:]) and (pas[i] in duplicates):
##        duplicates[i]+=1
##    if (pas[i] in pas[i+1:]) and (pas[i] not in duplicates):
##        duplicates[i]=0
##        
##
##hint_given=[]
##while True:
##    p=input("Enter password:")
##    if p==pas:
##        print("Successfully Matched Password!!")
##        break
##    else:
##        print("Incorrect Password!!")
##        hints=[]
##        for i in p:
##            if i in hint_given and i in duplicates:
##                print(f"Password does contain multiple {i} 's")
##                duplicates[i]-=1
##                
##            if i in pas:
##                hints.append(i)
##        
##        if not hints:
##            print("None of the characters are present,\nTry different combination.")
##        else:
##          
##            for i in hints:
##                if i not in hint_given:
##                    print("Password does contain:",i)
##                    hint_given.append(i)
                    
    


# Take a number , provide hint in which direction is
##the number is 

##s=106
##
##while True:
##    n=int(input("Enter number:"))
##    if n==s:
##        print("Successfully found the number!!")
##        break
##    else:
##        if n<s:
##            print("Number is greater")
##        else:
##            print("Number is lower")
    
    


##for i in range(1,10):
##    if i%2==0:
##        continue
##    print(i)

# WAP to find the sum of all the numbers present in a list
# but skip prime numbers

ls=[1,2,3,4,5,6]
##s=0
##for i in ls:
##    flag=True
##    if i in [1,2]:
##        continue
##    
##    for j in range(2,i):
##        if i%j==0:
##            flag=False
##            break
##    
##    if flag:
##        s+=i
##print(s)

##a=[7,29,4,35,17,45]
##for i in a:
##    flag=True
##    for j in range(2,i)


# Wap to find the distinct 2nd largest number

a=[1,6,2,2,11,9,11,9,5]


l=a[0]
sl=float('-inf')

for i in a:
    if a.count(i)>1:
        continue
    if i>l:
        sl=l
        l=i
    elif l>i>sl:
        sl=i
        

print(ls[-2])
        
    









