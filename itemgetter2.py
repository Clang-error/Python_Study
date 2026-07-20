from operator import itemgetter

# students = [("jane",22,'A'),("dave",32,'B'),("sally",17,'B')]
students = [{"name": "jane", "age": 22, "grade":'A'},{"name": "dave","age":32,"grade":'B'},{"name":"sally","age":32,"grade":'C'}]
result = sorted(students,key=itemgetter('age'))
print(result)
