# Sample tuple for demonstration
my_tuple = (5, 2, 8, 6, 2, 9, 2)

# i) len() - returns the number of elements in the tuple
print("Length of the tuple:", len(my_tuple))

# ii) count(x) - returns the number of times x appears in the tuple
print("Count of 2 in tuple:", my_tuple.count(2))

# iii) index(x) - returns the index of the first occurrence of x
print("Index of first occurrence of 8:", my_tuple.index(8))

# iv) sorted() - returns a new sorted list from the tuple elements
sorted_tuple = sorted(my_tuple)
print("Sorted tuple (as list):", sorted_tuple)

# v) min() - returns the smallest element
print("Minimum value in tuple:", min(my_tuple))

# vi) max() - returns the largest element
print("Maximum value in tuple:", max(my_tuple))

# vii) cmp() - Not available in Python 3, so we define our own
# Let's define two tuples to compare
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)

# Custom comparison function (like cmp in Python 2)
def cmp(x, y):
    return (x > y) - (x < y)

comparison_result = cmp(tuple_a, tuple_b)
print("Comparison result (cmp equivalent):", comparison_result)
# Output: -1 means tuple_a < tuple_b, 0 means equal, 1 means greater

# viii) reversed() - returns an iterator that accesses the tuple in reverse order
reversed_tuple = tuple(reversed(my_tuple))
print("Reversed tuple:", reversed_tuple)
