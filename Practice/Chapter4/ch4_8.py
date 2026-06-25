#입력값을 모두 더해 출력하기

import sys
args = sys.argv[1:]
result = 0
for i in args:
    try:
        result += int(i)
    except ValueError:
        print("이건 못먹는다.")
print(result)
