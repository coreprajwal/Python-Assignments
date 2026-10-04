# IF Questions

# Check if a number is positive

##num=int(input("Enter number:"))
##
##if num>0:
##    print("Number is postive")


# Check if a number is divisible by 5

##num=int(input("Enter number:"))
##
##if num%5==0:
##    print("Number divisible by 5")


# Check if age is eligible to vote
##age=int(input("Enter age:"))
##if age>=18:
##    print("Eligible to vote.")


# Check if a number is even
##num=int(input("Enter number:"))
##
##if num@2==0:
##    print("Number is even.")


# Check is a character is uppercase
##character=input("Enter character:")
##if character.isupper():
##    print("Character is upper.")

# Check if a number is greater than 100

##num=int(input("Enter number:"))
##
##if num>100:
##    print("Number is greater than 100")


# Check if a string length is more than 10

##string=input("Enter string:")
##
##if len(string)>10:
##    print("String length more than 10.")

# Check if a year is a leap (Only basic condition divisible by 4)

##year=int(input("Enter year:"))
##if year%4==0:
##    print("Its a leap year.")

# Check if temperature is above 30

##temp=int(input("Enter temperature:"))
##if temp>30:
##    print("Temperature is greater than 30 degrees.")


# Check if a number is multiple of both 3 and 7

##num=int(input("Enter number:"))
##if num%3==0 and num%7==0:
##    print("Number is divisible by both 3 and 7")






## If-Else Questions:

# Check if a number is even or odd

##num=int(input("Enter number:"))
##if num%2:
##    print("Number is Odd.")
##else:
##    print("Numbe is Even.")


# Check if a number is positive or negative

##num=int(input("Enter number:"))
##
##if num>=0:
##    print("Number is positive.")
##else:
##    print("Number is negative.")


# Check if a character is vowel or consonant

##character=input("Enter character:")
##
##if character.upper() in "AEIOU":
##    print("Character is vowel.")
##else:
##    print("Character is consonant.")


# Check if a student passed (>=40) or failed.

##marks=int(input("Enter marks:"))
##
##if marks>=40:
##    print("You passed the test.")
##else:
##    print("You failed.")


# get two numbers and print the larger one

##num1=int(input("Enter number 1:"))
##num2=int(input("Enter number 2:"))
##
##if num1>num2:
##    print(num1,"Num1 is greater.")
##else:
##    print(num2,"Num2 is greater.")



# Check if a number is divisible by 2 or not

##num=int(input("Enter number:"))
##
##if num%2:
##    print("Number is not divisible by 2.")
##else:
##    print("Number is divisible by 2.")



# Check if a person is minor or not

##age=int(input("Enter age:"))
##if age>=18:
##    print("You are an adult.")
##else:
##    print("You are a Minor.")


# Check if entered password matches predefined password.

##password="prajwal@2003"
##pass_=input("Enter password:")
##
##if pass_==password:
##    print("Passoword matched.")
##else:
##    print("Invalid password.")

# Check whether a given number is greater than 50 or not

##num=int(input("Enter number:"))
##if num>50:
##    print("Number is greater than 50.")
##else:
##    print("Lesser than 50.")

# Check if a number is within range 1-100.

##num=int(input("Enter number:"))
##if 1<num<100:
##    print("Number is within 1-100.")
##else:
##    print("Number is not in range 1-100.")


# Check if a number is divisible by 3 but not by 5.

##num=int(input("Enter number:"))
##if num%3==0 and num%5!=0:
##    print("Number is divisible by 3 but not by 5")
##else:
##    print("Number is either not divible by 3 or divisible by .")


# Check if a number is within range 10-50 but exclude 25.

##num=int(input("Enter number:"))
##if 10<num<50 and num!=25:
##    print("Number is in range of 10-50 excluding 25.")
##else:
##    print("Number is either not in range 10-50 or is 25")


# Check if a character is alphabet but not vowel

##char_=input("Enter character:")
##if char_.isalpha and char_.upper() not in "AEIOU":
##    print("Character is alphabet but not a vowel")
##else:
##    print("Character is either not alphabet or is vowel")


# Check if a number is 2 digit palindrome or not

##num=int(input("Enter number:"))
##if 9<num<100 and num%10==num//10:
##    print("Number is 2 digit and also a palindrome")
##else:
##    print("Either not a 2 digit number or not a palindrome.")

# Check if a person is eligible for discount (age<18 or age>60)
# and purchase >500

##age=int(input("Enter age:"))
##purchase=int(input("Enter purchase amount:"))
##
##if (age<18 or age>60) and (purchase>500):
##    print("Eligible for discount.")
##else:
##    print("Not eligible for discount.")

# Given a number print "weird" if its odd or in range(6-20) even
# Otherwise print "Not weird"

##num=int(input("Enter number:"))
##if num%2 and 6<=num<=20:
##    print("Number is odd and in range 6-20")
##else:
##    print("Either a even number or not in range 6-20")

##Check if a year is a leap year or not using full leap year condition

##year=int(input("Enter year:"))
##if (year%4==0 and year%100!=0) or (year%400==0):
##    print("Its a leap year.")
##else:
##    print("Its not a leap year.")


# Check if 3 numbers can form a triangle

##side1=int(input("Enter side 1:"))
##side2=int(input("Enter side 2:"))
##side3=int(input("Enter side 3:"))
##
##if side1+side2==side3 and side2+side3==side1 and side3+side1==side2:
##    print("Three sides can form a triangle")
##else:
##    print("Three sides cannot form a triangle.")


# Check if two strings are equal ignoring cases

##string1=input("Enter first string:")
##string2=input("Enter second string:")
##
##if string1.lower()==string2.lower():
##    print("Both strings are equal.")
##else:
##    print("Both strings are not equal.")


# Validate password length is >=8 and contains digits.


##password= input("Enter password:")
##if len(password)>=8 and password.isalnum() and not password.isalpha():
##    print("Password length is greter than equal to 8 and contains digits.")
##else:
##    print("Either lesser than 8 characters or does not contain digits.")


##Write a program to print python is greater than java for 5 times

##i=1
##while i<6:
##    print("Python is greater than Java.")


# If-elif-else:

## Grade system based on marks (90+, 75+, 50+, else fail)

##marks=int(input("Enter marks:"))
##
##if marks<0 or marks>100:
##    print("Invalid marks.")
##elif marks>=90:
##    print("Grade A")
##elif marks>=75:
##    print("Grade B")
##elif marks>=50:
##    print("Grade C")
##else:
##    print("Fail")

# Find largest amonge three members

##num1=int(input("Enter 1st member:"))
##num2=int(input("Enter 2nd member:"))
##num3=int(input("Enter 3rd member:"))
##
##if num1>num2 and num1>num3:
##    print(num1,"Num1 is highest")
##elif num2>num1 and num2>num3:
##    print(num2,"Num2 is highest")
##elif num3>num1 and num3>num2:
##    print(num3,"Num3 is highest")
##else:
##    print("Number is invalid.")

# Check if a year is a leap year or not

##year=int(input("Enter year:"))
##
##if (year%4==0 and year%100!=0)) or year%400==0:
##    print("Its a leap year")
##else:
##    print("Its not a leap year")

# Categorize age (Child, teen,adult, senior citizen )

##age=int(input("Enter Age:"))
##
##if 0<age<12:
##    print("Child")
##elif 12<age<18:
##    print("Teen")
##elif 18<age<61:
##    print("Adult")
##elif age>60:
##    print("Senior citizen")
##else:
##    print("Invalid age")


# Check if a number is positive , negative or zero

##num=int(input("Enter number:"))
##
##if num>0:
##    print("Positive number")
##elif num<0:
##    print("Negative number")
##else:
##    print("Number is zero.")

# Simple calculator based on user choice

##op1=int(input("Enter operand 1:"))
##opr=input("Enter operator:")
##op2=int(input("Enter operand 2:"))
##
##if opr=='+':
##    print(op1+op2)
##elif opr=='-':
##    print(op1-op2)
##elif opr=='/':
##    print(op1/op2)
##else:
##    print(op1*op2)


#Identity day of the week based on number (1-7)
##num=int(input("Enter number:"))
##map_week={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",1:"Saturday"}
##
##print(map_week[num])

##ATM withdrawal check (balance > amount, insufficient, zero balance).

##bal=int(input("Enter balance:"))
##amt=int(input("Enter amount:"))
##
##if bal>=amt:
##    print("Deduction successfull, remaining balance:",bal-amt)
##    bal-=amt
##elif amt>bal:
##    print("Insufficient balance")
##else:
##    print("Invalid amount")


##Check traffic signal color (red, yellow, green).




##Categorize BMI value.

##h=int(input("Enter your height:"))
##w=int(input("Enter your weight:"))
##bmi=w/h**2
##
##if bmi<17:
##    print("Under weight")
##elif 17<bmi<25:
##    print("Moderate weight")
##else:
##    print("Overweight")


##Mini electricity bill calculator (different rates for 0–100, 101–300, 300+ units).

##units=float(input("Enter electricity units:"))
##if 0<units<101:
##    print("Your bill is:",units*6)
##elif 100<units<301:
##    print("Your bill is:",units*7)
##elif units>300:
##    print("Your bill is:",units*8)
##else:
##    print("Enter valid units.")


##Student grading with distinction logic (90+, 75+, 50+, borderline 48–49 → re-evaluation).

##grd=int(input("Enter grades:"))
##if grd<0 or grd>100:
##    print("Invalid grades")
##elif grd>90:
##    print("A+")
##elif grd>75:
##    print("B+")
##elif grd>50:
##    print("C+")
##elif grd in (48,49):
##    print("Apply for revaluation.")
##else:
##    print("Fail")



##ATM withdraw system (invalid amount, insufficient balance, successful).
##bal=int(input("Enter balance:"))
##amt=int(input("Enter Amount:"))
##
##if amt<0:
##    print("Invalid amount")
##elif bal>amt:
##    print("Withdraw successfull, remaining balance:",bal-amt)
##    bal-=amt
##else:
##    print("Insufficient balance to withdraw.")

    

##Find second largest among three numbers.
##a=int(input("Enter 1st number:"))
##b=int(input("Enter 2nd number:"))
##c=int(input("Enter 3rd number:"))
##
##if a>b>c or c>b>a:
##    print(b,"is 2nd largest.")
##elif b>c>a or a>c>b:
##    print(c,"is 2nd largest.")
##elif b>a>c or c>a>b:
##    print(a,"is 2nd largest.")
##else:
##    print("Invalid or equal numbers")

   

##BMI calculator with underweight / normal / overweight / obese.
##w=float(input("Enter weight (kg):"))
##h=float(input("Enter height (m):"))
##
##bmi=w/h**2
##
##if bmi<10 or bmi>30:
##    print("Invalid input.")
##elif bmi<=17.5:
##    print("underweight:",bmi)
##elif bmi<23:
##    print("Normal",bmi)
##elif bmi<25:
##    print("overweight",bmi)
##else:
##    print("Obese",bmi)



##Ticket pricing (weekday price,
##weekend price, senior discount).

##weekday=("monday","tuesday","wednesday","thursday","friday")
##weekend=("sunday","saturday")
##
##day=input("Enter day:")
##age=int(input("Enter age:"))
##
##if (day not in weekday) and (day not in weekend) and (age<0 or age>110):
##    print("Enter right day and age")
##if age>60:
##    print("Price is 100rs")
##elif day in weekday:
##    print("Price is 200 rs")
##elif day in weekend:
##    print("Price is 150rs")



##Rock-Paper-Scissors game logic.
##u1=input("Enter user 1 move:")
##u2=input("Enter user 2 move:")
##rps_map={"rock":"paper", "paper":"scissors","scissors":"rock"}
##
##if (u1 not in rps_map.keys()) or (u2 not in rps_map.keys()):
##    print("Enter valid moves")
##elif rps_map[u1]==u2:
##    print("u2 wins")
##elif rps_map[u2]==u1:
##    print("u1 wins")
##else:
##    print("Draw..go home")


##Income tax slab calculation.

##sal=float(input("Enter monthly salary:"))*12
##
##
##if 0<sal<=1200000:
##    print("No tax -- enjoy for a little while")
##elif 1200000<sal<=1600000:
##    print("30% tax -- cry a little")
##elif 1600000<sal<2500000:
##    print("35 % tax -- need handkerchief?")
##else:
##    print("40% tax -- + We'll not give you proper roads. ;) ")


##Check if quadratic equation has real, equal, or imaginary roots.
##a=int(input("Enter equations x square coefficient:"))
##b=int(input("Enter equations x coefficient:"))
##c=int(input("Enter equations constant:"))
##
##d=b**2-4*a*c
##
##if d>0:
##    print("Has 2 real and unequal roots")
##elif d==0:
##    print("Has 2 real equal roots")
##else:
##    print("Has imaginary roots")


##Categorize temperature (freezing, cold, warm, hot, extreme).
##t=int(input("Enter temperature:"))
##if t<-120 or t>60:
##    print("Print valid temperature")
##elif t<=0:
##    print("Freezing")
##elif t<=23:
##    print("Cold")
##elif t<=30:
##    print("warm")
##elif t<=45:
##    print("hot")
##else:
##    print("Extreme")


##
##4. Nested if (10 Questions)
##Check if number is positive AND even.

##n=int(input("Enter number:"))
##if n>0:
##    if n%2:
##        print("positive odd")
##    else:
##        print("positive even")
##else:
##    print("Negative")

    
##Login system (check username → then password).

##u=input("Enter username:")
##p=input("Enter password:")
##username="prajwal"
##password="prajwal@123"
##
##if u==username:
##    if p==password:
##        print("Succefull login")
##    else:
##        print("password is wrong")
##else:
##    print("username is wrong")

##Check largest among three numbers using nested if.
##a=int(input("Enter number 1:"))
##b=int(input("Enter number 2:"))
##c=int(input("Enter number 3:"))
##
##if a>b:
##    if a>c:
##        print(a,":a is greater")
##elif b>a:
##    if b>c:
##        print(b,":b is greater")
##else:
##    print(c,":c is greater")


##Bank loan eligibility (age check → income check).

##a=int(input("Enter age:"))
##i=int(input("Enter income:"))
##
##if 18<=a<=30:
##    if 300000<i<=700000:
##        print("Eligible for loan.")
##    else:
##        print("not eligible")
##elif 30<=a<=60:
##    if 700000<i:
##        print("Eligible for loan.")
##    else:
##        print("not eligible")
##else:
##    print("Not eligible")


##Check if year divisible by 4 → then divisible by 100 → then 400.
##y=int(input("Enter year:"))
##
##if y%4==0:
##    if y%100!=0:
##        print("Leap year")
##    else:
##        if y%400==0:
##            print("Leap year")
##        else:
##            print("Not leap year")
##else:
##    print("Not a leap year")



##Check triangle type after validating sides.

##a=int(input("Enter side a:"))
##b=int(input("Enter side b:"))
##c=int(input("Enter side c:"))
##
##if a+b>c and b+c>a and a+c>b:
##    if  a==b==c:
##        print("Its equilateral triangle")
##    elif a==b or b==c or c==a:
##        print("Its isolateral triangle")
##    elif a!=b!=c:
##        print("Its scalen triangle")
##    else:
##        print("Triangle without name")
##else:
##    print("Triangle not possible")



##Employee bonus eligibility (experience → performance rating).
##e=int(input("Enter experience:"))
##r=int(input("Enter performance rating (out of 5):"))
##
##
##if 5<e<=20:
##    if 3<=r<=5:
##        print("Eligible")
##    else:
##        print("Not eligible")
##else:
##    print("Not eligible")


##Student scholarship (marks → family income).

##m=int(input("Enter marks:"))
##i=int(input("Enter family income:"))
##
##if m>80:
##    if 0<i<=50000:
##        print("Eligble scholarship")
##    elif i<=100000:
##        print("Eligible + 5k extra amount")
##    else:
##        print("Not eligible")
##else:
##    print("Not eligible")



##Check if character is alphabet → then check uppercase/lowercase.
##c=input("Enter character:")
##if c.isalpha():
##    if c.isupper():
##        print("upper case")
##    else:
##        print("lower case")
##else:
##    print("Character other than alphabet")


##E-commerce discount system (cart amount → membership type).
##cm=int(input("Enter cart amount:"))
##m=int(input("Membership type (Premium:1,Best:2,Normal:3):"))
##
##if cm>2000:
##        if m<0 or m>3:
##            print("Invalid membership")
##        elif m==1:
##            print("30% discount, final amount:",cm-cm*(30/100))
##        elif m==2:
##            print("20% discount, final amount:",cm-cm*(20/100))
##        else:
##            print("10% discount, final amount:",cm-cm*(10/100))
##else:
##    print("Required cart amount not reached!!")

##Login system with 3 attempts only.

##u=input("Enter username:")
##p=input("Enter password:")
##
##username="prajwal"
##password="prajwal@123"
##
##if u==username:
##    if p==password:
##        print("Login successfull")
##    else:
##        print("Wrong password, Remaining attempt: 2",)
##        p=input("Enter password:")
##        if p==password:
##            print("Login successfull")
##        else:
##            print("Again Wrong password, Remaining attempt: 1",)
##            p=input("Enter password:")
##            if p==password:
##                print("Login successfull")
##            else:
##                print("You have timed out.")
##else:
##    print("Wrong username")
            


##Loan approval:
##Age ≥ 21
##Salary ≥ 25k
##If salary < 40k → need guarantor

##a=int(input("Enter age:"))
##s=int(input("Enter salary:"))
##
##if a>=21:
##    if s<40000:
##        print("Need guarantor")
##    elif s>=25000:
##        print("Loan approved")
##
##else:
##    print("Not approved")


##Validate triangle and then check its type (equilateral / isosceles / scalene).

##a=int(input("Enter side a:"))
##b=int(input("Enter side b:"))
##c=int(input("Enter side c:"))
##
##if a+b>c and b+c>a and a+c>b:
##    if  a==b==c:
##        print("Its equilateral triangle")
##    elif a==b or b==c or c==a:
##        print("Its isolateral triangle")
##    elif a!=b!=c:
##        print("Its scalen triangle")
##    else:
##        print("Triangle without name")
##else:
##    print("Triangle not possible")


##E-commerce discount:
##Cart > 1000 → 10%
##If prime member → additional 5%

##cm=int(input("Enter cart amount:"))
##m=int(input("Are you a Prime Member?(Yes:1, No:0):" ))
##
##if cm>1000:
##        if m!=0 and m!=1:
##            print("Invalid membership detail")
##        elif m==1:
##            print("15% discount for Prime Member, final amount:",cm-cm*(15/100))
##        else:
##            print("10% discount, final amount:",cm-cm*(10/100))
##else:
##    print("Required cart amount not reached!!")




##Scholarship system:
##Marks ≥ 85
##Family income < 5 lakh
##If marks ≥ 95 → bonus stipend

##m=int(input("Enter marks:"))
##i=int(input("Enter family income:"))
##
##if m>=85:
##    if 0<i<=500000:
##        if m>=95:
##            print("Eligible for scholarship + Extra stipend.")
##        else:
##            print("Eligible for scholarship")
##    
##    else:
##        print("Not eligible")
##else:
##    print("Not eligible")




##Check if number is prime using nested condition.

##n=int(input("Enter number:"))
##
##i=2
##flag=True
##output="Prime number"
##while i<n and flag:
##    if n%i==0:
##        output="Not a prime number"
##        falg=False
##    i+=1
##print(output)

##University admission logic (cutoff + entrance test
##+ reserved category).

##e=int(input("Enter entrance marks:"))
##c=input("Enter category:")
##cat=["obc","scst","general"]
##
##if c in cat:
##    if c=="scst":
##        if e>=60:
##            print("Admission succesfull (scst)")
##        else:
##            print("Admission failed (scst) ")
##    elif c=="obc":
##        if e>=80:
##            print("Admission succesfull (obc)")
##        else:
##            print("Admission failed (obc)")
##    else:
##        if e>=95:
##            print("Admission succesfull (general)")
##        else:
##            print("Admission failed (general)")
##        
##
##else:
##    print("Invalid Category.")




##Car insurance eligibility (age + accident history).

##a=int(input("Enter age:"))
##ah=int(input("How many accidents history noted?:"))
##
##if 30<=a<=50:
##    if 0<ah<2:
##        print("Eligible")
##    else:
##        print("Not eligible")
##else:
##    print("Not eligible")
    



##Multi-level password validation (length → digit
##→ special char).

##p=input("Enter password:")
##
##if len(p)>=8:
##    
##    if p.isalnum() and not p.isalpha():
##        if not p.isalnum():
##            print("Password created.")
##        else:
##            print("Please include special characters")
##    else:
##        print("Please include digits.")
##
##else:
##    print("Password lenght is less than 8")



##Check if a date is valid (day-month-year basic check).


##d=int(input("Enter day:"))
##m=input("Enter month:")
##y=int(input("Enter year:"))
##
##b_m=["jan","mar","may","jul","aug","oct","dec"]
##
##
##if m in b_m:
##    if 0<d<32:
##        print("Valid")
##    else:
##        print("Not valid")
##else:
##    if m=="feb":
##        if (y%4==0 and y%100!=0) or y%400==0:
##            if 0<d<30:
##                print("Valid")
##            else:
##                print("Not Valid")
##        else:
##            if 0<d<29:
##                print("Valid")
##            else:
##                print("Not Valid")
##            
##    else:
##        if 0<d<31:
##            print("Valid")
##        else:
##            print("Not valid")







































































































