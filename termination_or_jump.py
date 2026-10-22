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

pw="prajwal123"

while True:
    i=input("Enter password:")
    if pw==i:
        break
print("Succesfully Entered")






Wap to take password verify whether the password is correct or not ,
if password is not correct , then give hint to the user,
with every newly entered password give a new hint
