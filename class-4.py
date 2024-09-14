name = input("Enter your name: ")
age = int(input("Enter your age: "))

print('Welcome {}!, your name is {} and you are {} years old.'.format(name, name, age))

num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))

print("Summation of {} and {} is : {}".format(num_1, num_2, (num_1 + num_2)))

print("Substraction of {} and {} is : {}".format(num_1, num_2, (num_2 + num_1)))

if num_1 > num_2: print("{} is greater than {}.".format(num_1, num_2))
elif num_1 == num_2: print("{} is equal to {}.".format(num_1, num_2))
else: print("{} is less than {}".format(num_1, num_2))

subject = input("Enter your subject: ")
mark = int(input("Enter mark you got: "))
result = ""
if(mark > 79): result = "A+"
elif(mark > 69): result = "A"
elif(mark > 59): result = "A-"
elif(mark > 55): result = "B"
elif(mark > 49): result = "B-"
elif(mark > 39): result = "C"
elif(mark > 32): result = "D"
else: result = "F"

print("You got {} in {}".format(result, subject))

num_1 = int(input("Enter a number to check even or odd: "))
if(num_1 % 2 == 0): print("{} is even: ".format(num_1))
else: print("{} is odd.".format(num_1))

num_1 = float(input("Enter 1st number: "))
num_2 = float(input("Enter 2nd number: "))
num_3 = float(input("Enter 3rd number: "))
num_4 = float(input("Enter 4th number: "))
num_5 = float(input("Enter 5th number: "))
print("Smallest number from {}, {}, {}, {} and {} is: {}".format(num_1, num_2, num_3, num_4, num_5, min(num_1, num_2, num_3, num_4, num_5)))