# Python Program to Demonstrate Set Operations

# Initial Set
set_a = {1, 2, 3}
print("Initial Set A:", set_a)

# i) add()
set_a.add(4)
print("\nAfter add(4):", set_a)

# ii) update()
set_a.update([5, 6], {7, 8})
print("After update([5, 6], {7, 8}):", set_a)

# iii) copy()
set_b = set_a.copy()
print("\nCopied Set B from A:", set_b)

# iv) pop()
popped_element = set_a.pop()
print("\nAfter pop(), removed element:", popped_element)
print("Set A after pop():", set_a)

# v) remove()
set_a.remove(5)  # Will raise KeyError if element doesn't exist
print("\nAfter remove(5):", set_a)

# vi) discard()
set_a.discard(10)  # No error if element is not found
print("After discard(10):", set_a)

# vii) clear()
set_c = {10, 20, 30}
print("\nOriginal Set C:", set_c)
set_c.clear()
print("After clear(), Set C:", set_c)

# Create two sets for set operations
set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}

# viii) union()
set_union = set_x.union(set_y)
print("\nSet X:", set_x)
print("Set Y:", set_y)
print("Union of X and Y:", set_union)

# ix) intersection()
set_intersection = set_x.intersection(set_y)
print("Intersection of X and Y:", set_intersection)

# x) difference()
set_difference = set_x.difference(set_y)
print("Difference of X - Y:", set_difference)
