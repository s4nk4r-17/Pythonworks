
#Employee
#id,name,age,salary,department

class Employee:

    id:int

    name:str

    age:int

    salary:int

    department:str

    def set_employee(self,id,name,age,department,salary):
        
        self.id=id

        self.name=name

        self.age=age

        self.department=department

        self.salary=salary

    def display_emp(self):

        print(self.id,self.name,self.age)

#reference_name=ClassName()

emp_instance=Employee()

emp_instance.set_employee(101,"John",26,"hr",34421)

emp_instance.display_emp()