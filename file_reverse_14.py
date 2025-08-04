# Replace 'sample.txt' with the path to your file
filename = 'sample.txt'

with open(filename, 'r') as file:
    for line in file:
        # Strip the newline character and reverse the line
        reversed_line = line.rstrip('\n')[::-1]
        print(reversed_line)
