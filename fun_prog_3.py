
# Demonstration of id(), type(), and range()

# Using type() to check the data type

a = [1, 2, 3]

print("Using type():")
print(f"The type of a is: {type(a)}")
print()

# Using id() to get memory address (identity) of objects
print("Using id():")
print(f"The id of a is: {id(a)}")
print()

# Using range() to create a sequence of numbers
print("Using range():")
for i in range(10):
    print(i,end=" ")

