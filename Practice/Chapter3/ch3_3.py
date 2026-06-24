#별 표시하기

i = 0

while True:
    i+=1
    if i > 5: break
    for num in range(i): print("*", end="")
    print()


i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i) #이렇게도 가능함