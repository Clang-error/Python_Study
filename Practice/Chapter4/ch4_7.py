with open("/Users/clang_error/01.Python/Practice/Chapter4/test4.txt",'r') as f:
    body = f.read()

body = body.replace("java","python")

with open("/Users/clang_error/01.Python/Practice/Chapter4/test4.txt",'w') as f:
    f.write(body)