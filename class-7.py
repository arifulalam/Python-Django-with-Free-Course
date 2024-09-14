# File Read/Write

file = open("data.txt", "w")
file.writelines("Name\t: Ariful Alam")
file.writelines("\nAge\t: 40")
file.writelines("\nEmail\t: ariful-alam@hotmail.com")
file.close()

file = open("data.txt", "r")
output = file.read()
file.close()

file = open("data.txt", 'a')
file.writelines("\nUsername: arifulalam")
file.close()

file = open("data.txt", "r")
output = file.read()
file.close()

print(output)

#Error Handling

list = [1, 2, 5, 6, 3, 7]

try:
    print(list[10])
except IndexError:
    print("Trying to access a value in a possition which not exists.")

try:
    input = int(input('Enter a string (aplhanumaric) value: '))
    print(input)
except ValueError:
    print("Your entered value is not a integer")
except TypeError:
    print("You entered wrong value. You should enter integer value")

try:
    print(5/0)
except ZeroDivisionError:
    print('You tried to devide a number by zero (0) which is not possible')

