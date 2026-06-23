print("=" * 50)
print("My program")
print("=" * 50)

a = "Life is too short"
print(len(a))
print(a[0:4])

a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

arr="Pithon"
arr=arr[:1] + "y" + arr[2:]
print(arr)

number= 10
day = "three"
print("I ate %d apples. so I was sick for %s days" % (number, day))