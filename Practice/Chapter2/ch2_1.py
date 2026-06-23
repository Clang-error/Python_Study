#평균 점수 구하기

subject = {"이름":"홍길동","국어":80, "영어":75, "수학":55}

sum = subject.get("국어") + subject.get("영어") + subject.get("수학")
avg = sum / 3
print(subject.get("이름"))
print(avg)
