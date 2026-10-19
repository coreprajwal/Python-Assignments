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
##13.	Count frequency of each character in string.
##14.	Print all prime numbers between 1 and 100.
##15.	Find common elements between two lists (without intersection method).
##16.	Find pairs in list whose sum = target value.
##17.	Rotate list by K positions.
##18.	Find missing number in 1–N list.
##19.	Check if two strings are anagrams (without sorting).
##20.	Check Armstrong numbers between 1–500.
##________________________________________while Loop (10 Questions)
##1.	Print numbers from 1 to N.
##2.	Sum of digits of a number.
##3.	Reverse a number.
##4.	Check palindrome number.
##5.	Print Fibonacci series up to N terms.
##6.	Keep asking password until correct one is entered.
##7.	Count number of digits in a number.
##8.	Find GCD of two numbers.
##9.	ATM system (loop until user exits).
##10.	Guessing game (loop until correct guess).
##11.	Reverse number and check palindrome.
##12.	Keep asking user until valid email format entered.
##13.	Create simple number guessing game with limited attempts.
##14.	Find factorial using while loop.
##15.	Fibonacci until value exceeds 1000.
##16.	ATM simulation until exit option selected.
##17.	Count number of prime digits in a number.
##18.	Convert decimal to binary manually.
##19.	Calculate power without using ** operator.
##20.	Keep dividing number by 2 until it becomes 1.
