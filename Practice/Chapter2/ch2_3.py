#주민등록번호 나누기

pin = "881120-1068234"
yyyymmdd = "19"+pin[:2]+pin[2:4]+pin[4:6]
num = pin.split("-")[1]
print(yyyymmdd)
print(num)