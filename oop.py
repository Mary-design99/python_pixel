#class Student:
    #name="Mary"
    #age="21"
#student1=Student()
#print(f"name of student is:{student1.name}")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1=Student("Eric",22)
student2=Student("Mary" ,21)
print(f"my name is {student1.name} i am {student1.age} years old")
print(f" my friend is {student2.name} she is {student2.age} years old")
