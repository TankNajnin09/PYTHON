from datetime import datetime

# Ask for user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Get the current year
current_year = datetime.now().year

# Calculate the year when the user will turn 60
year_turn_60 = current_year + (60 - age)

# Print the message
print(f"{name}, you will turn 60 years old in the year {year_turn_60}.")
