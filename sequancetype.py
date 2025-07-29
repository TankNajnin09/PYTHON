
#string

s="Welcome to KSC"
print("String = ",s)
print("First character of string = ",s[0])
print("Avoid first character of string = ",s[1:])
print("Second to seven character of string = ",s[2:7])
print("Last character of string = ",s[-1])
print("Second last character of string = ",s[-2])
print("")
print("")

#bytes type

element = [10,20,30,40]
b=bytes(element)
print(b)

print(b[0])

for i in b:
    print(i,end=" ")
print("")
print("")

#Bytearray type
    
c=bytearray(element)
for i in c:
    print(i,end=" ")
print("")
c[0]=100
for i in c:
    print(i,end=" ")
print("")
print("")

#list type

a=[10,20,30,"ksc","pac",-10,200.10]
print(a)
for i in a:
    print(i,end=" ")
print("")
print(a[2:6])
print(a[-1])
print(a[1:4])
print("")

#tuple type

t=(10,20,30,40,50)
print(t)
print(type(t))
print(t[0])
print("")

#range type

a=range(1,50,2)
print(a)
for i in a:
    print(i,end=" ")
