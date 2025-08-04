
#list() method
a=list((10,20,20,10,30))
print("Create a list using list() = ",a)

#len() method
li_len=len(a)
print("Length of list = ",li_len);

#append() method

a.append(60)
print("Append() metod =",end=" ")
print(a)

#copy() method

b=a.copy()
print("Copy() metod =",end=" ")
print(b)

#count() method

print("Count() method total 10 =",a.count(10))

#extend() method

a.extend([50,60])
print("After extend =",a)

#index() method

print("Index() method =",a.index(30))

#insert() method

a.insert(2,400)
print("After insert =",a)

#pop() method

a.pop()
a.pop()
print("Pop() metod =",end=" ")
print(a)

#remove() method

a.remove(20)
print("After remove =",a)

#reverse() method

a.reverse()
print("Reverse() method =",a)

#sort() method

a.sort()
print("After sorting =",a)

#clear() method

a.clear()
print(a)
print("All elements are clear...")


