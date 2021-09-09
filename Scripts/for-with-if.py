# my_num = int(input("Enter your lucky number: "))
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for X in  my_list:
#     if (X == my_num):
#         print("You choose: ", X)
#     else:
#         print("Select the numbers which are there in the list")

#Program to find out the entered value is there in the list or not
# a=int(input("enter value"))
# b= [1,2,3,4]
# if a in b:
#     print("yes")
# else:
#     print("no")

fruits = ["mango", "Banana", "grapes", "papaya"]
my_fav = str(input("Enter your fav fruit name: "))

if my_fav in fruits:
    print("Your fav fruit is:", my_fav)
else:
    print("Choose from the list")