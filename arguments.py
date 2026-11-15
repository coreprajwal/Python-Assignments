##WAP to display details of a user and take details as a
## variable length keyword argument
## name and age is mandatory

def user(*,name=0,age=0,**kwargs):
    if name or age:
        print("Enter name and age")
    else:
        print(kwargs)

##flag=True
##while flag:
##    key=input("Enter key:")
##    value=input("Enter value:")
##    
##    exitt=int(input("Enter 1 to exit and 0 to continue:"))
##    if exitt:
##        flag=False
    
user(name="prajwal",age="33",occupation="navy")
