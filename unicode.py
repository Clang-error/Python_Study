
text = input("유니코드로 변환할 문장또는 단어를 입력해주세요:")

Unicode=[]
next = 0
for i in text:
    Unicode.append(ord(i))
    
print(Unicode)

hexcode = []
for i in Unicode:
    hexcode.append(hex(i))

print(*hexcode)