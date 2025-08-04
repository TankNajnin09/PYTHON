# Sample string
text = "Hello, Python!"

print("Original string:", text)

# i) Accessing using Indexing

# Positive indexing (0-based)
print("\nIndexing with positive indices:")
print("First character (index 0):", text[0])
print("Seventh character (index 6):", text[6])
print("Last character (index 12):", text[12])

# Negative indexing (starts from -1 at the end)
print("\nIndexing with negative indices:")
print("Last character (index -1):", text[-1])
print("Second last character (index -2):", text[-2])
print("Eighth character from the end (index -6):", text[-6])

# ii) Accessing using Slice Operator

print("\nSlicing examples:")

# Slice from start to index 4 (excluding 5)
print("text[0:5]:", text[0:5])  # 'Hello'

# Slice from index 7 to end
print("text[7:]:", text[7:])  # 'World!'

# Slice entire string
print("text[:]:", text[:])  # 'Hello, World!'

# Slice with negative indices
print("text[-6:-1]:", text[-6:-1])  # 'World'

# Slice with step (every 2nd character)
print("text[::2]:", text[::2])  # 'Hlo ol!'

# Slice with negative step (reversing string)
print("text[::-1]:", text[::-1])  # '!dlroW ,olleH'

# Slice with start, stop, and step
print("text[1:10:3]:", text[1:10:3])  # 'e,W'

