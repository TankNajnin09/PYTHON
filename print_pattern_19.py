
#pyramid of 1 to 10
print("pyramid of 1 to 10 : ")
n = 5
for i in range(1, n + 1):
    print(str(i) * i)
print()
print()

#pyramid of A to Z
print("pyramid of A to Z : ")
n = 5
for i in range(1, n + 1):
    for j in range(i):
        # chr(65) is 'A'
        print(chr(65 + j), end=' ')
    print()
print()
print()

#pyramid of *
print("pyramid of * : ")
n = 5
for i in range(n, 0, -1):
    print('*' * i)
