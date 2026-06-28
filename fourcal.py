class Fourcal:
    def __init__(self, first,second):
        self.first = first
        self.second = second

    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result=self.first + self.second
        return result
    def mul(self):
        result= self.first * self.second
        return result
    def sub(self):
        result= self.first - self.second
        return result
    def div(self):
        try:
            result = self.first / self.second
        except(ZeroDivisionError):
            print("0입니다잉")
            result = 0
        return result

class morefourcal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourcal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = morefourcal(4,0)
b = SafeFourcal(4,0)
print(a.pow())
print(a.div())
print(b.add())
print(b.div())


# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())
