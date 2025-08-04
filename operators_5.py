#arithmetic operator
a=10
b=20

print("Arithmetic Operator:")
print("Addition = ",a+b)
print("Substriction = ",a-b)
print("Multiplication = ",a*b)
print("Division = ",a/b)  
print("Modulus:", a % b) 
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
print()
print()

#assignment operator
print("\nAssignment Operator:")
a+=b
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)
print()
print()

#Relational operator
print("\nRelational Operator:")

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print()
print()

#logical operator
print("\nLogical Operator:")
x=1;y=2;z=3 
if(x>y and y>z):
    print('X is big')
elif(y>x and y>z):
    print('Y is big')
else:
    print('Z is big')
print()
print()

#Bitwise operator
print("\nBitwise Operator:")
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
print()
print()

#ternary operator
print("\nTernary Operator:")
a, b = 10, 20
min = a if a < b else b
print("Minimum value is =",min)
