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
    def __str__(self):
        return f"student {self.name} {self.gender} {self.nationality} {self.age}"
    def __lt__(self,other):
        return self.age < other.age
    def __le__(self,other):
        return self.age <= other.age
    def __eq__(self,other):
        return self.age == other.age

stu_1=Student("John","男","China",18)
print(stu_1)
stu_2=Student("Kane","男","England",33)
stu_3=Student("Ming","女","China",34)
if stu_2.__lt__(stu_1):
    print(f"{stu_2.name}比{stu_1.name}更小")
else:
    print(f"{stu_2.name}比{stu_1.name}更大")
if stu_3.__le__(stu_2):
    print(f"{stu_3.name}比{stu_2.name}小于或等于")
else:
    print(f"{stu_3.name}比{stu_2.name}大")
if stu_3.__eq__(stu_2):
    print(f"{stu_3.name}={stu_2.name}")
else:
    print(f"{stu_3.name}!={stu_2.name}")