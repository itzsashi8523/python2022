user_input = input("Enter your Age: ")
#print(user_input.isnumeric())
if user_input.isnumeric() != True:
    print("Enter Only Numbers / Only Numbers are Supported")
else:
    print("Your Age is:", user_input)
#####isnumeric() is a method which returns the type of a input value, it returns boolian value like True or False

# if type (user_input) != int:
#     print("enter a number")
# if type (user_input) != int:
#     print("Correct only integer values")
# elif user_input == 35:
#     print("Correct Age")
# elif user_input < 35:
#     print("Lesser Age, not eligible")
# else:
#     print("Invalid Age")