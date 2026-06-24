f = open("/Users/clang_error/01.Python/test.txt",'w')
for i in range(1,11):
    data = f"{i}번째 줄입니다 \n"
    f.write(data)
f.close()

f = open("/Users/clang_error/01.Python/test.txt",'r')
line = f.readline()
print(line)
f.close()

f = open("/Users/clang_error/01.Python/test.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()


