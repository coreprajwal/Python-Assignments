##for Loop (10 Questions)

##1.	Print numbers 1 to 10.

##for i in range(1,11):
##    print(i)

##2.	Print even numbers from 1 to 50.

##for i in range(1,51):
##    if i%2==0:
##        print(i)

##3.	Find sum of first N numbers.
##n=int(input("Enter number:"))
##s=0
##for i in range(1,n+1):
##    s+=i
##print(s)

##4.	Print multiplication table of a number.
##n=int(input("Enter number:"))
##for i in range(1,11):
##    print(f"{n}*{i}={n*i}")

##5.	Count digits in a number (using string loop).
##n=int(input("Enter number:"))
##c=0
##for i in str(n):
##    c+=1
##print(c)

##6.	Reverse a string using loop.

##r=""
##s="hello"
##
##for i in s:
##    r=i+r
##print(str(r))


##7.	Count vowels in a string.
##v="aeiou"
##s="hello world"
##s=s.lower()
##r={}
##for i in s:
##    if i in v:
##        if i not in r.keys():
##            r[i]=1
##        else:
##            r[i]+=1
##print(r)

##8.	Print factorial of a number.

##n=int(input("Enter number:"))
##fs=[]
##i=2
##
##while n!=0 and i<=n:
##    if n%i==0:
##        fs.append(i)
##        n=n//i
##        i=1
##    i+=1
##    
##print(fs)



##9.	Find largest number in a list.


##ls=[3,8,1,2,9,3]
##l=float('-inf')
##for i in ls:
##    if i>l:
##        l=i
##print(l)
    


##10.	Print elements at even index positions.

##ls=[3,8,1,2,9,3]
##for i in range(0,len(ls),2):
##    print(ls[i])



##11.	Find second largest number in a list .

##ls=[7,7,7,7]
##
##l=float("-inf")
##sl=float("-inf")
##
##for i in ls:
##    if i>l:
##        sl=l
##        l=i
##    elif l>i>sl:
##        sl=i
##
##        
##if sl==float("-inf"):
##    print("No second highest")
##else:
##    print(f"{sl} is the second highest")



##12.	Remove duplicate elements from list (without using set).
##ls=[1,2,3,2,4,6,6]
##u=[]
##for i in ls:
##    if i not in u:
##        u.append(i)
##print(u)


##13.	Count frequency of each character in string.

##s="Hello this is prajwal"
##d={}
##for i in s:
##    
##    if i not in d:
##        d[i]=1
##    else:
##        d[i]+=1
##print(d)

##14.	Print all prime numbers between 1 and 100.

##n=100
##p=[]
##
##for i in range(2,n):
##    flag=True
##    for j in range(2,i):
##        if i%j==0:
##            flag=False
##        
##    if flag:
##        p.append(i)
##print(p)
    


##15.	Find common elements between two lists (without intersection method).

##ls1=[1,2,3,4,5]
##ls2=[4,5,6,7,8]
##r=[]
##for i in ls1:
##    if i in ls2:
##        r.append(i)
##print(r)


##16.	Find pairs in list whose sum = target value.
##    (Solve Again)

##target=9
##ls=[1,2,3,4,5]
##p=[]
##for i in ls:
##    if target-i in ls:
##        p.append((i,target-i))
##        ls.remove(i)
##        ls.remove(target-i)
##print(p)

##17.	Rotate list by K positions.

##ls=[1,2,3,4]
##k=int(input("Enter number:"))
##p=k%len(ls)
##for i in range(p):
##    ls.insert(0,ls[-1])
##    ls.pop()
##print(ls)


##18.	Find missing number in 1–N list.

##ls=[1,3,4,5,7]
##m=[]
##for i in range(len(ls)-1):
##    if ls[i+1]-ls[i]!=1:
##        for j in range(1,(ls[i+1]-ls[i])):
##            m.append(ls[i]+j)
##print("Missing numbers:",m)


##19.	Check if two strings are anagrams (without sorting).
##ana=input("Enter string 1:")
##ana2=input("Enter string 2:")
##flag=True
##for i in ana:
##    if (i not in ana2) and ana2.count(i)!=ana.count(i):
##        flag=False
##if flag:
##    print("Its an anagram")
##else:
##    print("Its not an anagram")
    

##20.	Check Armstrong numbers between 1–500.



##--------------while Loop (10 Questions)-------------------

##1.	Print numbers from 1 to N.
##n=int(input("Enter number:"))
##for i in range(1,n+1):
##    print(i)

##2.	Sum of digits of a number.
##n=123
##s=0
##for i in str(n):
##    s+=int(i)
##print(s)

##n=123
##s=0
##
##while n>0:
##    s+=n%10
##    n=n//10
##print(s)
    

##3.	Reverse a number.

##n=123
##res=0
##while n>0:
##    rem=n%10
##    res=res*10+rem
##    n=n//10
##    
##print(res)

##4.	Check palindrome number.

##n1=int(input("Enter number 1 :"))
##n2=int(input("Enter number 2 :"))
##rev=0
##while n1>0:
##    rem=n1%10
##    rev=rev*10+rem
##    n1=n1//10
##if n2==rev:
##    print("Its a palindrome",rev)
##else:
##    print("Not a palindrome")



##5.	Print Fibonacci series up to N terms.

##n=int(input("Enter number:"))
##res=1
##for i in range(1,n+1):
##    res=res*i
##print(res)

##6.	Keep asking password until correct one is entered.
##pwd="prajwal123"
##flag=True
##while flag:
##    p=input("Enter passoword:")
##    if p==pwd:
##        print("Correct password")
##        flag=False
##    else:
##        print("Wrong password, Enter again")

    
##7.	Count number of digits in a number.
##n=int(input("Enter number:"))
##c=0
##while n>0:
##    n=n//10
##    c+=1
##print(c)
    

##8.	Find GCD of two numbers.

##n1=int(input("Enter number 1:"))
##n2=int(input("Enter number 2:"))
##
##
##if n2>n1:
##    s=n1
##    l=n2
##else:
##    s=n2
##    l=n1
##
##for i in range(s,0,-1):
##
##    if s%i==0 and l%i==0:
##        print(i,"is GCD!")
##        break


##9.	ATM system (loop until user exits).
##users={"prajwal":"pass@123"}
##flag=True
##while flag:
##    i=input("Enter username:")
##    if i in users:
##        print("User found Successfully!!")
##        flag=False
##        break
##    print("User not found!")

##10.	Guessing game (loop until correct guess).
##rn=88
##while True:
##    n=int(input("Enter input:"))
##    if n==rn:
##        print("You guessed it Right!!! Congrats!")
##        break
##    print("Wrong guess, try again ---")

##11.	Reverse number and check palindrome.
##ori_n=int(input("Enter number:"))
##n=ori_n
##res=0
##while n:
##    rem=n%10
##    res=res*10+rem
##    n=n//10
##if ori_n==res:
##    print("Its a palindrome")
##else:
##    print("Its not a palindrome")


##12.	Keep asking user until valid email format entered.

##while True:
##    e=input("Enter valid email address:")
##
##    if e.islower() and e[:len(e)-10].isalnum() and e.find("@gmail.com")>0:
##        print("Email accepted.")
##        break
##    print("format not matched!!")


##13.	Create simple number guessing game with limited attempts.
##guess=6
##attempt=10
##while attempt:
##    n=int(input("Enter number:"))
##    if n==guess:
##        print("Successfully Guessed!")
##        break
##    print("Try Again!!")
##    attempt-=1


##14.	Find factorial using while loop.

##ori_n=int(input("Enter number:"))
##n=ori_n
##f=1
##while n:
##    f*=n
##    n-=1
##print(f)

##15.	Fibonacci until value exceeds 1000.



##16.	ATM simulation until exit option selected.
##17.	Count number of prime digits in a number.
##18.	Convert decimal to binary manually.

##19.	Calculate power without using ** operator.
##n=int(input("Enter base value:"))
##e=int(input("Enter exponent value:"))
##temp=n
##for i in range(1,e):
##    temp*=n
##print("Exponent answer is :",temp)

##20.	Keep dividing number by 2 until it becomes 1.



