##Write a program to write "Python is greater than java" for 5 times

##i=1
##while i<6:
##    print("Python is greater than Java.")
##    i+=1

##Write a program to print even numbers between 1 to 10

##i=1
##while i<11:
##    if i%2==0:
##        print(i)
##    i+=1


## Write a program to find sum of n even numbers

#Solution 1:
##i=1
##n=int(input("Enter number:"))
##sum_=0
##while i<=n:
##    sum_+=i*2
##    i+=1
##print(sum_)

#Solution 2:

##n=int(input("Enter number:"))
##sum_=0
##m=2
##i=1
##while i<=n:
##    sum_+=m
##    m+=2
##    i+=1
##print(sum_)

# Solution 3:

##n=int(input("Enter number:"))
##sum_=0
##i=1
##while i<=n:
##    sum_+=i*2
##    i+=1
##print(sum_)

# Write a program to get sum of n odd numbers

##n=int(input("Enter number:"))
##sum_=0
##i=1
##odd_c=1
##while odd_c<=n:
##    sum_+=i
##    odd_c+=1
##    i+=2
##print(sum_)


# WAPT calculate the sum of n natural number

##n=int(input("Enter number:"))
##i=1
##sum_=0
##while i<=n:
##    sum_+=i
##    i+=1
##print(sum_)


# WAP to check if all the element of a list is a even number or not






# WAP to find sum of even numbers till/between 1 to n


##n=int(input("Enter number:"))
##i=1
##sum_=0
##while i<n:
##    if i%2==0:
##        sum_+=i
##    i+=1
##print(sum_)

# WAP to find the sum of all the palindrome between 1 to 100

##n=100
##i=1
##s=0
##while i<n:
##    if str(i)[::-1]==str(i):
##        s+=i
##    i+=1
##
##print(s)


# WAP to check if the sum of all the numbers
#in a list is even number or not

##ls=[1,2,3]
##
##i=0
##s=0
##
##while i<len(ls):
##    s+=ls[i]
##    i+=1
##    
##if s%2==0:
##    print("Even")
##else:
##    print("Odd")


# Check if all elements of list are even or odd.

##ls=[2,3,6 , 9]
##
##i=0
##s=0
##flag="contains even"
##
##while i<len(ls):
##    if ls[i]%2==1:
##        flag="Contains odd"
##    i+=1
##    
##print(flag)

# WAP to print sum of the element in 2 lists
##
##ls1=[5,1]
##ls2=[3,2,1]
##
##s1=0
##s2=0
##
##i=0
##while i<len(ls1):
##    s1+=ls1[i]
##    i+=1
##    
##i=0
##while i<len(ls2):
##    s2+=ls2[i]
##    i+=1
##print(s1+s2)


## WAP to find if 2nd largest number in a list is even or odd
##idx=0
##ls=[5,1,1,9,4,7]
##l_n=0
##i=0
##while i<len(ls):
##    if ls[i]>l_n:
##        l_n=ls[i]
##        idx=i
##    i+=1
##ls.pop(idx)
##l_2=0
##i=0
##while i<len(ls):
##    if ls[i]>l_2:
##        l_2=ls[i]
##        idx=i
##    i+=1
##if l_2%2:
##    print("2nd largest is odd.")
##else:
##    print("2nd largest is Even.")

# From the given string create list having each word of string as
# element without using .split()

##s="this is python string"
##ls=[]
##s_s=0
##i=0
##while i<len(s):
##    if s[i]==" ":
##        ls.append(s[s_s:i])
##        s_s=i+1
##    if i==len(s)-1:
##        ls.append(s[s_s:i+1])
##
##    i+=1
##print(ls)

# WAP to check if a number is palindrome or not without using
# typecasting

##num=int(input("Enter number:"))
##n=num
##i=0
##flag=True
##while flag:
##    rem=n%10
##    print("pass:",i,"current number:",n,"remainder:",rem)
##    n=n-rem
##    if rem==0:
##        lst=1
##        flag=False
##    i+=1
##
##digits=i+1
##print("Total digits:",digits)
##total_digit=eval("1"+"0"*(digits-1))
##loop=True
##palindrome="Not sure yet"
##while loop:
##    if num==0:
##        print("Got remainder zero, doing loop=False")
##        loop=False
##    elif (num%10==num//total_digit):
##        print("current number:",num,"Last position==",num%10,"First position:",num//total_digit)
##        num=(num-(num%10))/10
##        print("removed last digit, current number:",num)
##        print("Current num:",num,"Removing first position number, total_digit:",total_digit/10,"removing :",total_digit/10)
##        num= (num//(total_digit/10))
##        print("Current number:",num,"Removed first digit:",num,"subtracting from total_digit:",total_digit)
##        palindrome="Its a palindrome"
##    else:
##        palindrome="Not a palindrome"
##        loop=False
##        
##print(palindrome)



# WAP which prints how many odd numbers, even numbers and negative numbers are present in a list

##ls= [1,2,-5,-3,6,-2]
##odd_count=0
##neg_count=0
##i=0
##while i<len(ls):
##    if ls[i]%2:
##        odd_count+=1
##    if ls[i]<0:
##        neg_count+=1
##
##    i+=1
##even_count=len(ls)-odd_count
##print("Odd count:",odd_count,"\nEven count:",even_count,"\nNegative count:",neg_count)
        

# WAP to check how many names in a list starts with a vowel

##ls=["Prajwal","Akash","Vikas","Pankaj","Om"]
##vowel_count=0
##
##i=0
##while i<len(ls):
##    if ls[i][0].upper() in "AEIOU":
##        vowel_count+=1
##    i+=1
##conso_count=len(ls)-vowel_count
##
##print("Vowel"
##      "count:"
##      ,vowel_count)
##print("Consonant count:",conso_count)

        
# WAP to print how many even length string is present in a list

##ls=[1,2,"hello","World","guys"]
##o_c=0
##e_c=0
##i=0
##while i<len(ls):
##    if type(ls[i])==type(""):
##        if len(ls[i])%2:
##            o_c+=1
##        else:
##            e_c+=1
##    i+=1
##print(f"Even count :{e_c}, Odd count: {o_c}")

# WAP to check if the given numbers is gcd (Greatest common divisor) or not

##n1=int(input("Enter number 1:"))
##n2=int(input("Enter number 1:"))
##
##gcd=0
##i=1
##
##while i<=n2:
##    if n1%i==0 and n2%i==0:
##        gcd=i
##    i+=1
##
##print("Gcd is:",gcd)


# WAP to check if the given numbers is lcm (least common divisor) or not

##n1=int(input("Enter number 1:"))
##n2=int(input("Enter number 1:"))
##
##flag=True
##i=1
##lcm=0
##flag=True
##while flag:
##    if (i*n1)%n2==0:
##        lcm=i*n1
##        flag=False
##
##    i+=1
##print("Lcm:",lcm)

##solution 2:
##print(a*b//gcd)



# WAP to check if a give number is a palindrome or not
# without type casting or slicing



##num=int(input("Enter a number:"))
##orginal_n=num
##n_num=0
##
##while num:
##    rem=num%10 ##remainder
##    n_num=n_num*10+rem
##    num=num//10 # removing last digit
##
##
##if n_num==orginal_n:
##    print(n_num)
##    print("Its a palindrome")
##else:
##    print(n_num)
##    print("Its not a palindrome")
    




#Wap program to find number of digit in an integer.


##num=int(input("Enter nummber:"))
##count=0
##i=0
##while num:
##    rem=num%10
##    count+=1
##    num=num//10
##    i+=1
##
##print(count)
    



#Wap program to check if a number is an armstrong number.


num=int(input("Enter nummber:"))
org_n=num
count=0
i=0
while num:
    rem=num%10
    count+=1
    num=num//10
    i+=1

res=0
temp=org_n
while org_n:
    rem=org_n%10
    res+=rem**count
    org_n=org_n//10
    

if res==temp:
    print("Armstrong number")
else:
    print("Not an armstrong number")





































    
