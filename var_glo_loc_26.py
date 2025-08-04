# Global variable
counter = 0

def increase():
    global counter  # Refer to the global variable
    count = 5
    counter += 1  # Refer to the local variable
    print("Inside increase() global variable counter =", counter)
    print("Inside increase() local variable count =", count)

print("Before calling increase() global variable counter =", counter)
increase()
print("After calling increase() global variable counter =", counter)
