# Control Transfer Statements in Python

# i) break statement

print("Example 1: break statement")
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at num =", num)
        break  # Exit the loop when num == 5
    print("Current number:", num)
print("Exited loop using break\n")

# ii) continue statement

print("Example 2: continue statement")
for num in range(1, 6):
    if num == 3:
        print("Skipping number 3")
        continue  # Skip the rest of the loop when num == 3
    print("Current number:", num)
print("Finished loop using continue\n")

# iii) pass statement

print("Example 3: pass statement")
for letter in "hello":
    if letter == "e":
        pass  # Do nothing here; placeholder
        print("Pass block executed for letter 'e'")
    print("Current letter:", letter)
print("Finished loop using pass")
