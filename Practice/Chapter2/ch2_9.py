a={}
b={}
c={}
d={}
a['name'] = 'python'
b[('a',)] = 'python'
# c[[1]] = 'python' <- 오류발생
# 키가 리스트라면 값이 불변하지 않기에 파이썬에서 허락하지않음
d[250] = 'python'

print(a)
print(b)
print(d)
