# number=[1,2,3,4,5]
# result=[]
# for n in number:
#     if n % 2 ==1:
#         result.append(n*2)

# 컴프리헨션 전 문법



number=[1,2,3,4,5]
result=[n * 2 for n in number if n % 2 != 0]
print(result)

# 컴프리헨션 후 문법