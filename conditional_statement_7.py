# Conditional Statements in Python

#Simple if statement

print("Example 1: if statement")
age = 20
if age >= 18:
    print("You are eligible to vote.\n")  # Executes only if condition is True

#if-else statement

print("Example 2: if-else statement")
marks = 45
if marks >= 50:
    print("You passed the exam.\n")
else:
    print("You failed the exam.\n")  # Executes if condition is False

#if-elif-else statement

print("Example 3: if-elif-else statement")
grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")  # Executes if all above conditions are False
