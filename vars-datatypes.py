#first_number = 6
#second_number = 8
#print(first_number+second_number)
#type(first_number)
#myFloat = 3.1514
#type(myFloat)
#print(4%2)
# a = 5
# b = 10
# a += b  # In this case b value gets added to a and new value of a is the sum of a & b
# print(a)
# print(b)
# ###
# one=10
# two=20
# type(one)          ; This is to print the type of variable/value, in this case its integer
# <class 'int'>
# myFloat = 3.2423
# type(myFloat)      ; float value
# <class 'float'>
# myDecision = str(input("Enter your decision: "))
# result = type(myDecision)   # ; boolian
# print(result)
#  # <class 'bool'>

print(type({}))
print(type([]) is not list)  #It gives the output a boolian value like True/False
print(type([]) is list)
print(type({}) is not list)
print(type(()) is not tuple)

a = ('one', 'two', 'three')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

print(x)
print(y)
print(z)