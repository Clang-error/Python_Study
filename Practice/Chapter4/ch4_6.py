# 사용자 입력 저장하기

user_input = input("저장할 내용을 입력하세요:")
with open("/Users/clang_error/01.Python/Practice/Chapter4/test3.txt",'a') as f:
    f.write(user_input)
    f.write("\n")