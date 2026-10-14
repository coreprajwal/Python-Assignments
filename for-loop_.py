##range
##for i in range(1,10):
##    print(i)

#Multi-value datatypes

##list
##for i in [1,2,3,4,5,6,7,8,9,10]:
##    print(i)

##tuple
##for i in (1,2,3,4,5,6,7,8,9,10):
##    print(i)

##set
##for i in {1,2,3,4,5,6,7,8,9,10}:
##    print(i)

##dict
##for i in {1:"11",2:"22",3:"33"}:
##    print(i)

##string
##for i in "String":
##    print(i)




#Singular datatypes ----(X)

#Int--------------- (x)
##for i in 4:
##    print(i)

##float---------------(x)
##for i in 4.6:
##    print(i)

##complex--------------(x)
##for i in 3+3j:
##    print(i)

##Boolean------------------(x)
##for i in True:
##    print(i)



##a=1
##b=2
##c=3
##
##
##for i in a,b,c:
##    print(i)
##
##
##print(a,b,c)

##wa code to access keys and values of dictionary using for loop


##dictt={1:"11",2:"22","hello":"world"}
##
##for i in dictt:
##    print(i,dictt[i])


##dictt={1:"11",2:"22","hello":"world"}
##
##for i in dictt.items():
##    print(i[0],i[1], sep=' :')




##Create a list of tuples and every tuple should have 3 values

##ls=[(2,3,4),(5,6,7),(8,9,10)]
##
##for i,j,k in ls:
##    print(i,j,k)

##Wap to calculate the sum of n natural numbers using for loop

##n=int(input("Enter number:"))
##s=0
##for i in range(1,n+1):
##    s+=i
##print(s)


#Print numbers from 1 to 10

##for i in range(1,11):
##    print(i)

# Print even numbers from 1 to 50

##for i in range(1,51):
##    if i%2==0:
##        print(i)


# print multiplication table of a number


##n=int(input("Enter number:"))
##for i in range(1,11):
##    print(f"{n}*{i}={n*i}")


#Count digits in a number (using string loop)


##n=int(input("Enter number:"))
##c=0
##for i in str(n):
##    c+=1
##print(c)
    

# WAP to rotate a list by k value without loop. *****************

##k=1
##l=[10,1,2,6,4,12]
##k=k%len(l)
##print(l[-k::]+l[:-k:])


# WAP to rotate a list by k value without loop.

##k=4
##ls=[1,2,3,4,5]
##
##for i in range(4):
##    ls.insert(0,ls.pop())
##
##print(ls)


# WAP to check if 2 strings are rotation of each other or not.

##st=input("Enter string:")
##strr=input("Enter rotated string:")
##
##if st in strr+strr and len(st)==len(strr):
##    print("Rotated")
##else:
##    print("Not rotated")


## not allowed to use in operator----- try this


##WAP to find a pair in a list
## who's sum is equal to the target element (sum equal to target element)
##        ***************************
##target=9
##ls=[10,20,30,-1,8,6,100,1]
##
##res=set()
##
##for i in ls:
##    if i<=target:
##        n=target -i
##        if n in ls:
##            res.add(((i,n)))
##            ls.remove(n)
####    else:
####        n=i - target
####        if n in ls:
####            res.append((i,n))
##
##
##print(list(res))


##l=[12,34,-3,10,8,3,6,1]
##t=9
##h=set()
##res=[]
##
##for i in l:
##    if t-i in h:
##        res.append((t-i,i))
##    h.add(i)
##print(i)
        


# Wap to check whether the given number is a power of 2 or not.
#with for loop






# Find common elements between two lists (without intersection)

##ls1=[1,2,2,3,4,5]
##ls2=[11,2,3,44,55]
##res=[]
##for i in range(len(ls1)):
##    if ls1[i] in ls2:
##        res.append(ls1[i])
##        ls2.remove(ls1[i])
##
##print(res)



# Wap to print all the element of 2 list without repeating any
##number--- no set, allowed single loop, no concatinate list

##ls= [1,2,3]
##ls2=[2,11,22,33]
##
##a=ls.copy()
##ls.extend(ls2)
##
##h=[]
##
##for i in ls:
##    if i not in h:
##        print(i)
##        h.append(i)

##ls= [1,2,3]
##ls2=[2,11,22,33]
##res=[]
##
##if len(ls)>=len(ls2):
##    temp_1=ls
##    temp_2=ls2
##else:
##    temp_1=ls2
##    temp_2=ls
##
##for i in range(len(temp_1)):
##    if i<len(temp_2) and (temp_2[i] not in res) and temp_1[i] not in res:
##        res.extend((temp_2[i],temp_1[i]))
##    else:
##        res.append(temp_1[i])
##print(res)


# Remove duplicate elements from list (without using set).

##org=[2,3,1,2,5,1,8]
##ls=org
##
##h=[]
##for i in ls:
##    if i not in h:
##        h.append(i)
##    else:
##        org.remove(i)
##
##print(org)

# Wap second largest number in a list. (no set)


##ls=[1,2,4,6,6]
##
##l=float('-inf')
##sl=float('-inf')
##
##
##for i in ls:
##    if i>l:
##        sl=l
##        l=i
##    elif l>i>=sl:
##        sl=i
##    
##if sl==float('-inf'):
##    print("No 2nd highest")
##else:
##    print(sl)





#Count frequency of each character in string.

##s='chaotic'
##temp=s.lower()
##f={}
##
##for i in s:
##    if i not in f.keys():
##        f[i]=1
##    else:
##        f[i]+=1
##print(f)




##WAP to convert uppercase string into lowercase without using methods
##s='BANA#%%NAaa'
##r=''
##
##for i in s:
##    if 'A'<=i<='Z':
##        r+=chr(ord(i)+32)
##    else:
##        r+=i
##print(r)

    
##WAP to check if a number is a power of 2 or not
# can't use bitwise,
##hint : don't use for loop


##n=2
##r=''
##i=0
##while n!=0:
##    r+=str(n%2)
##    n=n//2
##
##r=r[::-1]
##
##if int(r[0])==1 and int(r[1::])==0:
##    print("Power of 2")
##else:
##    print("Not a power of 2")


a=eval(input("Enter number:"))

i=a
while i>1 and i%2==0:
    i//=2

if i==1:
    print("power of 2")
else:

























    
        


























