# i) dict() - Creating a dictionary
student = dict(name="John", age=21, course="Computer Science")
print("Dictionary using dict():", student)

# ii) len() - Length of the dictionary
print("\nLength of dictionary using len():", len(student))

# iii) clear() - Removes all items from the dictionary
temp_dict = student.copy()
temp_dict.clear()
print("\nAfter clear():", temp_dict)

# iv) get() - Gets the value for a key, returns None (or default) if key doesn't exist
print("\nGet value of 'name':", student.get('name'))
print("Get value of 'grade' (non-existent key):", student.get('grade', 'Not Found'))

# v) pop() - Removes a specific key and returns its value
age = student.pop('age')
print("\nAfter pop('age'), value:", age)
print("Dictionary after pop:", student)

# vi) popitem() - Removes and returns the last inserted item
last_item = student.popitem()
print("\nAfter popitem(), item removed:", last_item)
print("Dictionary after popitem:", student)

# Re-initialize dictionary for remaining examples
student = {'name': 'John', 'age': 21, 'course': 'Computer Science'}

# vii) keys() - Returns a view of keys
print("\nKeys in dictionary:", list(student.keys()))

# viii) values() - Returns a view of values
print("Values in dictionary:", list(student.values()))

# ix) items() - Returns a view of key-value pairs
print("Items in dictionary:", list(student.items()))

# x) copy() - Returns a shallow copy of the dictionary
student_copy = student.copy()
print("\nCopied dictionary using copy():", student_copy)

# xi) update() - Updates dictionary with key-value pairs from another dict
student.update({'grade': 'A', 'age': 22})
print("\nAfter update({'grade': 'A', 'age': 22'}):", student)
