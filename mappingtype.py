d={101:'ABC',102:'XYZ',103:'PQR'}
print(d)
for i in d:
    print(i)
print(d.keys())
print(d.values())
del d[102]
print(d)

print()
print()

postal={'delhi':110001,'chennai':600001,'amreli':365601}
print(postal)
for city in postal:
    print(city,postal[city])
