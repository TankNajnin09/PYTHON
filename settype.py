
#set type

s={10,10,10,20,20,30,40,50}
print(s)
print(type(s))
s1=set("Hello")
print(s1)
s.update([60,70])
print(s)
s.remove(40)
print(s)
print("")

#frozenset type

s2={10,20,30,10,10,20,40,50}
fs=frozenset(s2)
print(fs)
print(type(fs))
