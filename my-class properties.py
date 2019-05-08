class Student(object):
    def __init__(self,name):
        self.name = name

student1 = Student('Bob')
student1.score = 90


class StudentObject(object):
    name= 'student'
student2 = StudentObject()
print(student2.name)