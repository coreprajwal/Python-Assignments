## Admission System

d={}

temp_entry={'prajwalpathade': {'details': {'First name': 'prajwal', 'Last name': 'pathade', 'father name': 'vishnu', 'mother name': 'sunanda', 'address': 'pune', 'permanent address': 'ahilyanagar', 'dob': '19-01-2003', 'phone no:': '8999231074', 'addhar no': '320583258205'}, 'active': True}}
d.update(temp_entry)

def admission_form():
    global d
    first_name=input("Enter First name:")
    last_name=input("Enter last name:")
    father_name=input("Enter father name:")
    mother_name=input("Enter mother name:")
    add=input("Enter address:")
    p_add=input("Enter permanent address:")
    dob=input("Enter dob:")
    phone=input("Enter phone no:")
    addhar=input("Enter addhar no:")
    f_name=first_name+last_name

    temp={f_name:{"details":{"First name":first_name,
     "Last name":last_name,
    "father name":father_name,
    "mother name":mother_name,
    "address":add,
    "permanent address":p_add,
    "dob":dob,
    "phone no:":phone,
    "addhar no":addhar},"active":True}}
    d.update(temp)
    
def admission_cancel():
    print("\nEnter following details to cancel admission:")
    first_name=input("First name of student:")
    last_name=input("Last name of student:")
    f_name=first_name+last_name
    d[f_name]["active"]=False


def active_students():
    print("\nEnter following details to know details of student:")
    first_name=input("First name of student:")
    last_name=input("Last name of student:")
    f_name=first_name+last_name

    if d[f_name]["active"]:
        print("---------Record Fetched--------------")
        print(d[f_name]["details"])
    else:
        print("\n-----------------Admission is Cancelled for the student--------------------")

while True:

    print('''
1)Add Admission
2)Cancel Admission
3)Active Students
4)Exit System''')
    option=int(input("Choose No. from above options:"))

    if option==1:
        admission_form()
        print("\n------------Admission done!!---------------")
    elif option==2:
        admission_cancel()
        print("\n------------Admmision Cancelled!!---------------")
    elif option==3:
        active_students()
    elif option==4:
        print("Thanks for using the system!!")
        break
    else:
        print("Enter valid input!!")


