a = [1,2,3,4]
print(a.count(5))
print(len(a))
print(str(a[2])+"hi")

print(a)
del a[0]
print(a)
del a[1:]
print(a)

a.append(2)
print(a)
a = [5,4,3,1,2]
print(a)
a.sort()
print(a)

b=[6,7,8]
a.extend(b)
print(a)