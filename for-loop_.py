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

st=input("Enter string:")
strr=input("Enter rotated string:")

if st in strr+strr and len(st)==len(strr):
    print("Rotated")
else:
    print("Not rotated")


## not allowed to use in operator----- try this

































