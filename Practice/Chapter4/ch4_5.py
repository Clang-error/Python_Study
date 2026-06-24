# f1 = open("/Users/clang_error/01.Python/Practice/Chapter4/test2.txt",'w')
# f1.write("Life is too short")


# f2 = open("/Users/clang_error/01.Python/Practice/Chapter4/test2.txt",'r')
# print(f2.read())
# f1을 닫지않아서 출력이 저장되지않아서 f2에서 출력할 수 없음
# 추가로 파일을 닫지않으면 메모리 누수가 발생할 수 있음


with open("/Users/clang_error/01.Python/Practice/Chapter4/test2.txt",'w') as f1:
    f1.write("Life is too sdhort")


with open("/Users/clang_error/01.Python/Practice/Chapter4/test2.txt",'r') as f2:
    print(f2.read())

    # 수정본