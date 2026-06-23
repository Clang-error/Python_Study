s=set([1,2,3,4,5,6])
s2=set([5,6,7,8,9,10])
print(s&s2)
print(s | s2)

s.add(7)
print(s)

a = [1,2,3,4]
while a:
    print(a.pop())