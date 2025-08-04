# 1. Creating a set using curly braces {}
set1 = {1, 2, 3, 4, 5}
print("Set using curly braces:", set1)

# 2. Creating a set using the set() constructor from a list
set2 = set([10, 20, 30, 40])
print("Set from list using set():", set2)

# 3. Creating a set using the set() constructor from a string
set3 = set("hello")
print("Set from string (unique characters):", set3)

# 4. Creating a set with duplicate elements (duplicates will be removed)
set4 = set([1, 2, 2, 3, 3, 3, 4])
print("Set with duplicates removed:", set4)

# 5. Creating a frozen set (immutable set)
frozen = frozenset([1, 2, 3])
print("Frozen set (immutable):", frozen)
