# For Loop

list = ['Bagladesh', 'UK', 'US', 'Pakistan', 'India', 'Indonasia']
print('Print each item in list')
for a in list:
    print(a)

print('all values in range up to 10')
for a in range(10):
    print(a)

print('print all values in range up to 10 from 5')
for a in range(5, 10):
    print(a)

print('print all in range up to 20 starting from 5 after incrementing 3 each time')
for a in range(4, 20, 3):
    print(a)

dic = {
    "name": "Ariful Alam",
    "city": "Chattogram",
}

print('print key value pair in dictionary')
for (key, value) in dic.items():
    print(key, value)

print('print all keys in dictionary')
for key in dic.keys():
    print(key)

print('print all values in dictionary')
for value in dic.values():
    print(value)

x = int(input("Enter 1st number: "))
y = int(input("Enter 1st number: "))
z = [x * 2, y * 5]

# User defined function 

def addition(x, y, z):
    sum_ = x + y
    print('summation of {} and {} is {}'.format(x, y, sum_))

    sum__ = sum(z)
    print('summation of {} and {} is {}'.format(z[0], z[1], sum__))

addition(x, y, z)