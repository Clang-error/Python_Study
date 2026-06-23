#주민등록번호 인덱싱

pin = "881120-1068234"
gender = pin.split("-")[1][0]

if gender == "1" or gender == "3":
    print(gender + "은 남성입니다.")
elif gender == "2" or gender == "4":
    print(gender + "은 여성입니다.")
