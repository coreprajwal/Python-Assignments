##Simple calculator based on user choice

##A=int(input("Input Operand 1:"))
##opr=input("Enter operation (+,-,*,/): ")
##B=int(input("Input Operand 2:"))


##Method 1:

##if opr=='+':
##    print(A+B)
##elif opr=='-':
##    print(A-B)
##elif opr=='*':
##    print(A*B)
##elif opr=='/':
##    print(A/B)
##else:
##    print("Invalid choice")

##Method 2:

##if opr in '+-/*':
##    var= str(A)+opr+str(B)
##    print(eval(var))

##Identify day of week based on number 1-7

##num=int(input("Enter number:"))
##map_days={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
##
##print(map_days.get(num,"Invalid input"))

##Atm withdrawl check

##balance=int(input("Enter balance:"))
##amnt=int(input("Enter amount to witdraw:"))
##
##if balance==0:
##    print("balance is zero.")
##elif balance>amnt:
##    print("Withdraw successfull",balance-amnt)
##elif balance<amnt:
##    print("Insufficient balance.")
##
##else:
##    print("Invalid input")


##Write a program to check whether 3 sides form a triangle or not if they can form a traingle equal, isoscelace, scalling


##sd1=int(input("Enter side 1:"))
##sd2=int(input("Enter side 2:"))
##sd3=int(input("Enter side 3:"))
##
##if not(sd1+sd2>sd3 and sd2+sd3>sd1 and sd1+sd3>sd2):
##    print("Can't form a triangel.")
##elif sd1==sd2==sd3:
##    print("Equilateral triangle")
##elif sd1==sd2 or sd1==sd3 or sd2==sd3:
##    print("Isosceles triagle")
##elif sd1!=sd2 and sd1!=sd3 and sd2!=sd3:
##    print("scalen triangle")
    
    












