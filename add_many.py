#들어오는 인수가 몇개인지 모를때.abs
def add_many(*args):
    result =0
    for i in args:
        result = result + i
    return result

a= add_many(1,3,4,5,6,7,8,9,9,0,7,66,5,)
print(a)