## Write a program to check if the number is 2 digit or not ,
## if it is 2 digit check if its palindrome or not


##num=int(input("Enter number:"))
##
##if len(str(num))==2:
##    if num%10==num//10:
##        print("Its palindrome.")
##    else:
##        print("Not a palindrome")
##else:
##    print("Not 2 digit.")


##Check if a date is a valid date or not


##d=int(input("Enter day:"))
##m=int(input("Enter month:"))
##y=int(input("Enter year:"))
##
##a=(1,3,5,7,8,10,12)
##
##if 0<d<31 and 0<m<13 and 0<y:
##
##    if m==2:
##        if (y%4==0 and y%100!=0) or y%400==0:
##            if d<29:
##                print("valid")
##            else:
##                print("invalid")
##        else:
##            if d<=28:
##                print("valid")
##            else:
##                print("invalid")
##    elif m in a:
##        if d<=31:
##            print("valid")
##        else:
##            print("invalid")
##    else:
##        print("30 days")
##else:
##    print("Not valid date")



## Write a program to check whether the user entered
## password contains special character or not and the length
## of the password should be greater than 8


##p=input("Enter password:")
##
##if p.isalnum():
##    print("No special characters")
##    if len(p)>8:
##        print("length greater than 8")
##    else:
##        print("length not greater than 8")
##
##else:
##    print("Contains special characters")

## Write a program to check if a number is a natural number or not
## and if it is a palindrome or not

##num=int(input("Enter number:"))
##
##if num>0:
##    if str(num)[::-1]==str(num):
##        print("Palindrome")
##    else:
##        print("Natural number but not a palindrome.")
##
##else:
##    print("Not a natural number")

































