class Student:
    name=None
    gender=None
    nationality=None
    age=None
    def __init__(self,name,gender,nationality,age):
        self.name=name
        self.gender=gender
        self.nationality=nationality
        self.age=age

stu_1=Student("John","男","China",18)
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.age)