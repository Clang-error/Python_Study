#평균점수구하기

A = [70,60,55,75,96,90,70,70,85,100]
total = 0
for score in A:
    total += score
average = total / len(A)

print(average)