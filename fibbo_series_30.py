# Ask the user for the number of terms
n = int(input("Enter the number of terms for the Fibonacci series: "))

# Initialize the first two terms
a, b = 0, 1
count = 0

print("Fibonacci series:")

# Generate the Fibonacci series
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
