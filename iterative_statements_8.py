# Iterative Statements in Python

# i) while loop

print("Example 1: while loop")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Increment to avoid infinite loop
print("Finished while loop\n")

# ii) for loop

print("Example 2: for loop")
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")
print("Finished for loop\n")

# Bonus: for loop with range()

print("Example 3: for loop with range()")
for i in range(1, 6):  # Prints numbers from 1 to 5
    print(f"Number: {i}")
print("Finished range-based for loop")
