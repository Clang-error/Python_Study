from faker import Faker

fake = Faker('Ko-KR')
fake.name()
print(fake.name())
print(fake.address())

for i in range(1,100):
    print(fake.address())