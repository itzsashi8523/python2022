user_age = input("Enter your Age: ")

print(user_age.isnumeric())

if user_age.isnumeric() == False:
    print("Invalid, Only Numbers are Allowed")
elif int(user_age) > 35:
    print("You are agebar candidate")
elif int(user_age) < 18:
    print("You are NOT eligible for this job")
else:
    print("Applied Successfully")
