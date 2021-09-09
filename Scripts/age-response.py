#Taking User's input of his age:
user_age = input("Enter your Age: ")

#This is just to print whether the entered value is numeric or not, It prints True if the given value is numeric, Prints False if the entered value is not a number(like string).
print(user_age.isnumeric())
print(user_age.isdigit()) #Working similar to isnumeric() method.

#Checking the condition, if user entered a number/string
if user_age.isnumeric() == False:
    print("Invalid, Only Numbers are Allowed")
elif int(user_age) > 35 and int(user_age) < 100:
    print("You are age-bar candidate")
elif int(user_age) < 18:
    print("You are NOT eligible for this job")
elif int(user_age) > 100:
    print("You are already died")
#If All OK, taking details from user and printing them finally.
else:
    f_name = input("Enter First Name: ")
    l_name = input("Enter Last Name: ")
    m_status = input("Enter M Status: ")
    print("Applied Successfully")
    print("Your Details Are: ", "\nFirst_Name:", f_name, "\nLast_Name:", l_name, "\nMarriage_Status:", m_status )
