# Function to return multiple values
def calculate_values(a, b):
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    return sum_val, diff_val, prod_val  # returning multiple values

# Calling the function
print("Example of return multiple values : \n")
x = 10
y = 5
result = calculate_values(x, y)

# Unpacking returned values
sum_result, diff_result, prod_result = result

# Displaying results
print("Input values: x =", x, ", y =", y)
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
