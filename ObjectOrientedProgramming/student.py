

#___________________________________________________________

#set_students()
#name,rollnumber,age,course

class Student:
    name:str
    rollnumber:str
    age:int
    course:str

    #initialiing attributes of student class

    def set_students(self,name,rollnumber,age,course):

        self.name=name

        self.rollnumber=rollnumber

        self.age=age
        
        self.course=course

    def display(self):

        print(self.name,self.rollnumber,self.age,self.course)

stu_instance=Student()

stu_instance.set_students("Roy",21,23,"B.com")

stu_instance.display()