def reverse_value(value):
    return value[::-1]

# Get user input
user_input = input("Enter a value to reverse: ")
print()

# Call the function and print the reversed value
reversed_value = reverse_value(user_input)
print("Original value:", reversed_value)
print("Reversed value:", reversed_value)
