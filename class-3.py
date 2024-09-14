# 16 July, 2024
# Operators

a = 10
b = 5
c = 13

# sumation of a and b
d = a + b
print("{} + {} = ".format(a, b), d);

# increase value of a by adding value of b
print("value of a ({}) increase by adding value of b ({})".format(a, b))
a += b
print("result is: {}".format(a))

# Comperison Operators

print('Is {} greater than {} : '.format(a, b), a > b)

print('Is {} less then {} : '.format(a, b), a < b)

print('Is {} is grater than {} and less then {} : '.format(a, b, c), a > b & a < c)

print('a ({}) to the power b ({}) = '.format(a, b), a ** b, pow(a, b))

A = a
a *= b
print('a ({}) multiplied by b ({})  = '.format(A, b), a)

d = a / c
print('A ({}) divided by b ({}) actual (with decimal value) = '.format(a, c), d)

d = a // c 
print('a ({}) divided by b ({}) actual (excluding decimal value) = '.format(a, c), d)

print('Is a ({}) fully dividable by b ({})?'.format(a, b), (a % b == 0))

print('Is a ({}) and b ({}) are equal? '.format(a, b), a is b)

print('Is a ({}) and b ({}) are not equal? '.format(a, b), a is not b)

